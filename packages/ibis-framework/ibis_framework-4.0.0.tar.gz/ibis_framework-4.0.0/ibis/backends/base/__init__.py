from __future__ import annotations

import abc
import collections.abc
import functools
import importlib.metadata
import keyword
import re
import sys
import urllib.parse
from pathlib import Path
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
)

if TYPE_CHECKING:
    import pandas as pd
    import pyarrow as pa

    import ibis.expr.schema as sch

import ibis
import ibis.common.exceptions as exc
import ibis.config
import ibis.expr.operations as ops
import ibis.expr.types as ir
from ibis import util

__all__ = ('BaseBackend', 'Database', 'connect')


class Database:
    """Generic Database class."""

    def __init__(self, name: str, client: Any) -> None:
        self.name = name
        self.client = client

    def __repr__(self) -> str:
        """Return type name and the name of the database."""
        return f'{type(self).__name__}({self.name!r})'

    def __dir__(self) -> list[str]:
        """Return the attributes and tables of the database.

        Returns
        -------
        list[str]
            A list of the attributes and tables available in the database.
        """
        attrs = dir(type(self))
        unqualified_tables = [self._unqualify(x) for x in self.tables]
        return sorted(frozenset(attrs + unqualified_tables))

    def __contains__(self, table: str) -> bool:
        """Check if the given table is available in the current database.

        Parameters
        ----------
        table
            Table name

        Returns
        -------
        bool
            True if the given table is available in the current database.
        """
        return table in self.tables

    @property
    def tables(self) -> list[str]:
        """Return a list with all available tables.

        Returns
        -------
        list[str]
            The list of tables in the database
        """
        return self.list_tables()

    def __getitem__(self, table: str) -> ir.Table:
        """Return a Table for the given table name.

        Parameters
        ----------
        table
            Table name

        Returns
        -------
        Table
            Table expression
        """
        return self.table(table)

    def __getattr__(self, table: str) -> ir.Table:
        """Return a Table for the given table name.

        Parameters
        ----------
        table
            Table name

        Returns
        -------
        Table
            Table expression
        """
        return self.table(table)

    def _qualify(self, value):
        return value

    def _unqualify(self, value):
        return value

    def drop(self, force: bool = False) -> None:
        """Drop the database.

        Parameters
        ----------
        force
            If `True`, drop any objects that exist, and do not fail if the
            database does not exist.
        """
        self.client.drop_database(self.name, force=force)

    def table(self, name: str) -> ir.Table:
        """Return a table expression referencing a table in this database.

        Parameters
        ----------
        name
            The name of a table

        Returns
        -------
        Table
            Table expression
        """
        qualified_name = self._qualify(name)
        return self.client.table(qualified_name, self.name)

    def list_tables(self, like=None, database=None):
        """List the tables in the database.

        Parameters
        ----------
        like
            A pattern to use for listing tables.
        database
            The database to perform the list against
        """
        return self.client.list_tables(like, database=database or self.name)


class TablesAccessor(collections.abc.Mapping):
    """A mapping-like object for accessing tables off a backend.

    Tables may be accessed by name using either index or attribute access:

    Examples
    --------
    >>> con = ibis.sqlite.connect("example.db")
    >>> people = con.tables['people']  # access via index
    >>> people = con.tables.people  # access via attribute
    """

    def __init__(self, backend: BaseBackend):
        self._backend = backend

    def __getitem__(self, name) -> ir.Table:
        try:
            return self._backend.table(name)
        except Exception as exc:  # noqa: BLE001
            raise KeyError(name) from exc

    def __getattr__(self, name) -> ir.Table:
        if name.startswith("_"):
            raise AttributeError(name)
        try:
            return self._backend.table(name)
        except Exception as exc:  # noqa: BLE001
            raise AttributeError(name) from exc

    def __iter__(self) -> Iterator[str]:
        return iter(sorted(self._backend.list_tables()))

    def __len__(self) -> int:
        return len(self._backend.list_tables())

    def __dir__(self) -> list[str]:
        o = set()
        o.update(dir(type(self)))
        o.update(
            name
            for name in self._backend.list_tables()
            if name.isidentifier() and not keyword.iskeyword(name)
        )
        return list(o)

    def _ipython_key_completions_(self) -> list[str]:
        return self._backend.list_tables()


# should have a better name
class ResultHandler:
    @staticmethod
    def _import_pyarrow():
        try:
            import pyarrow
        except ImportError:
            raise ModuleNotFoundError(
                "Exporting to arrow formats requires `pyarrow` but it is not installed"
            )
        else:
            return pyarrow

    @staticmethod
    def _table_or_column_schema(expr: ir.Expr) -> sch.Schema:
        from ibis.backends.pyarrow.datatypes import sch

        if isinstance(expr, ir.Table):
            return expr.schema()
        else:
            # ColumnExpr has no schema method, define single-column schema
            return sch.schema([(expr.get_name(), expr.type())])

    @util.experimental
    def to_pyarrow(
        self,
        expr: ir.Expr,
        *,
        params: Mapping[ir.Scalar, Any] | None = None,
        limit: int | str | None = None,
        **kwargs: Any,
    ) -> pa.Table:
        """Execute expression and return results in as a pyarrow table.

        This method is eager and will execute the associated expression
        immediately.

        Parameters
        ----------
        expr
            Ibis expression to export to pyarrow
        params
            Mapping of scalar parameter expressions to value.
        limit
            An integer to effect a specific row limit. A value of `None` means
            "no limit". The default is in `ibis/config.py`.
        kwargs
            Keyword arguments

        Returns
        -------
        Table
            A pyarrow table holding the results of the executed expression.
        """
        pa = self._import_pyarrow()
        try:
            # Can't construct an array from record batches
            # so construct at one column table (if applicable)
            # then return the column _from_ the table
            table = pa.Table.from_batches(
                self.to_pyarrow_batches(expr, params=params, limit=limit, **kwargs)
            )
        except ValueError:
            # The pyarrow batches iterator is empty so pass in an empty
            # iterator and a pyarrow schema
            schema = self._table_or_column_schema(expr)
            table = pa.Table.from_batches([], schema=schema.to_pyarrow())

        if isinstance(expr, ir.Table):
            return table
        elif isinstance(expr, ir.Column):
            # Column will be a ChunkedArray, `combine_chunks` will
            # flatten it
            if len(table.columns[0]):
                return table.columns[0].combine_chunks()
            else:
                return pa.array(table.columns[0])
        elif isinstance(expr, ir.Scalar):
            return table.columns[0][0]
        else:
            raise ValueError

    @util.experimental
    def to_pyarrow_batches(
        self,
        expr: ir.Expr,
        *,
        params: Mapping[ir.Scalar, Any] | None = None,
        limit: int | str | None = None,
        chunk_size: int = 1_000_000,
        **kwargs: Any,
    ) -> pa.ipc.RecordBatchReader:
        """Execute expression and return a RecordBatchReader.

        This method is eager and will execute the associated expression
        immediately.

        Parameters
        ----------
        expr
            Ibis expression to export to pyarrow
        limit
            An integer to effect a specific row limit. A value of `None` means
            "no limit". The default is in `ibis/config.py`.
        params
            Mapping of scalar parameter expressions to value.
        chunk_size
            Number of rows in each returned record batch.
        kwargs
            Keyword arguments

        Returns
        -------
        results
            RecordBatchReader
        """
        raise NotImplementedError


class BaseBackend(abc.ABC, ResultHandler):
    """Base backend class.

    All Ibis backends must subclass this class and implement all the
    required methods.
    """

    database_class = Database
    table_class: type[ops.DatabaseTable] = ops.DatabaseTable
    name: ClassVar[str]

    def __init__(self, *args, **kwargs):
        self._con_args: tuple[Any] = args
        self._con_kwargs: dict[str, Any] = kwargs

    def __getstate__(self):
        return dict(
            database_class=self.database_class,
            table_class=self.table_class,
            _con_args=self._con_args,
            _con_kwargs=self._con_kwargs,
        )

    def __hash__(self):
        return hash(self.db_identity)

    def __eq__(self, other):
        return self.db_identity == other.db_identity

    @functools.cached_property
    def db_identity(self) -> str:
        """Return the identity of the database.

        Multiple connections to the same
        database will return the same value for `db_identity`.

        The default implementation assumes connection parameters uniquely
        specify the database.

        Returns
        -------
        Hashable
            Database identity
        """
        parts = [self.table_class.__name__]
        parts.extend(self._con_args)
        parts.extend(f'{k}={v}' for k, v in self._con_kwargs.items())
        return '_'.join(map(str, parts))

    def connect(self, *args, **kwargs) -> BaseBackend:
        """Connect to the database.

        Parameters
        ----------
        args
            Mandatory connection parameters, see the docstring of `do_connect`
            for details.
        kwargs
            Extra connection parameters, see the docstring of `do_connect` for
            details.

        Notes
        -----
        This creates a new backend instance with saved `args` and `kwargs`,
        then calls `reconnect` and finally returns the newly created and
        connected backend instance.

        Returns
        -------
        BaseBackend
            An instance of the backend
        """
        new_backend = self.__class__(*args, **kwargs)
        new_backend.reconnect()
        return new_backend

    def _from_url(self, url: str) -> BaseBackend:
        """Construct an ibis backend from a SQLAlchemy-conforming URL."""
        raise NotImplementedError(
            f"`_from_url` not implemented for the {self.name} backend"
        )

    @staticmethod
    def _convert_kwargs(kwargs: MutableMapping) -> None:
        """Manipulate keyword arguments to `.connect` method."""

    def reconnect(self) -> None:
        """Reconnect to the database already configured with connect."""
        self.do_connect(*self._con_args, **self._con_kwargs)

    def do_connect(self, *args, **kwargs) -> None:
        """Connect to database specified by `args` and `kwargs`."""

    @util.deprecated(instead='use equivalent methods in the backend')
    def database(self, name: str | None = None) -> Database:
        """Return a `Database` object for the `name` database.

        Parameters
        ----------
        name
            Name of the database to return the object for.

        Returns
        -------
        Database
            A database object for the specified database.
        """
        return self.database_class(name=name or self.current_database, client=self)

    @property
    @abc.abstractmethod
    def current_database(self) -> str | None:
        """Return the name of the current database.

        Backends that don't support different databases will return None.

        Returns
        -------
        str | None
            Name of the current database.
        """

    @abc.abstractmethod
    def list_databases(self, like: str = None) -> list[str]:
        """List existing databases in the current connection.

        Parameters
        ----------
        like
            A pattern in Python's regex format to filter returned database
            names.

        Returns
        -------
        list[str]
            The database names that exist in the current connection, that match
            the `like` pattern if provided.
        """

    @staticmethod
    def _filter_with_like(
        values: Iterable[str],
        like: str | None = None,
    ) -> list[str]:
        """Filter names with a `like` pattern (regex).

        The methods `list_databases` and `list_tables` accept a `like`
        argument, which filters the returned tables with tables that match the
        provided pattern.

        We provide this method in the base backend, so backends can use it
        instead of reinventing the wheel.

        Parameters
        ----------
        values
            Iterable of strings to filter
        like
            Pattern to use for filtering names

        Returns
        -------
        list[str]
            Names filtered by the `like` pattern.
        """
        if like is None:
            return list(values)

        pattern = re.compile(like)
        return sorted(filter(lambda t: pattern.findall(t), values))

    @abc.abstractmethod
    def list_tables(
        self, like: str | None = None, database: str | None = None
    ) -> list[str]:
        """Return the list of table names in the current database.

        For some backends, the tables may be files in a directory,
        or other equivalent entities in a SQL database.

        Parameters
        ----------
        like : str, optional
            A pattern in Python's regex format.
        database : str, optional
            The database to list tables of, if not the current one.

        Returns
        -------
        list[str]
            The list of the table names that match the pattern `like`.
        """

    @functools.cached_property
    def tables(self):
        """An accessor for tables in the database.

        Tables may be accessed by name using either index or attribute access:

        Examples
        --------
        >>> con = ibis.sqlite.connect("example.db")
        >>> people = con.tables['people']  # access via index
        >>> people = con.tables.people  # access via attribute
        """
        return TablesAccessor(self)

    @property
    @abc.abstractmethod
    def version(self) -> str:
        """Return the version of the backend engine.

        For database servers, return the server version.

        For others such as SQLite and pandas return the version of the
        underlying library or application.

        Returns
        -------
        str
            The backend version
        """

    @classmethod
    def register_options(cls) -> None:
        """Register custom backend options."""
        options = ibis.config.options
        backend_name = cls.name
        try:
            backend_options = cls.Options()
        except AttributeError:
            pass
        else:
            try:
                setattr(options, backend_name, backend_options)
            except ValueError as e:
                raise exc.BackendConfigurationNotRegistered(backend_name) from e

    def compile(
        self,
        expr: ir.Expr,
        params: Mapping[ir.Expr, Any] | None = None,
    ) -> Any:
        """Compile an expression."""
        return self.compiler.to_sql(expr, params=params)

    def execute(self, expr: ir.Expr) -> Any:
        """Execute an expression."""

    def add_operation(self, operation: ops.Node) -> Callable:
        """Add a translation function to the backend for a specific operation.

        Operations are defined in `ibis.expr.operations`, and a translation
        function receives the translator object and an expression as
        parameters, and returns a value depending on the backend. For example,
        in SQL backends, a NullLiteral operation could be translated to the
        string `"NULL"`.

        Examples
        --------
        >>> @ibis.sqlite.add_operation(ibis.expr.operations.NullLiteral)
        ... def _null_literal(translator, expression):
        ...     return 'NULL'
        """
        if not hasattr(self, 'compiler'):
            raise RuntimeError('Only SQL-based backends support `add_operation`')

        def decorator(translation_function: Callable) -> None:
            self.compiler.translator_class.add_operation(
                operation, translation_function
            )

        return decorator

    def create_database(self, name: str, force: bool = False) -> None:
        """Create a new database.

        Not all backends implement this method.

        Parameters
        ----------
        name
            Name of the new database.
        force
            If `False`, an exception is raised if the database already exists.
        """
        raise NotImplementedError(
            f'Backend "{self.name}" does not implement "create_database"'
        )

    def create_table(
        self,
        name: str,
        obj: pd.DataFrame | ir.Table | None = None,
        schema: ibis.Schema | None = None,
        database: str | None = None,
    ) -> None:
        """Create a new table.

        Not all backends implement this method.

        Parameters
        ----------
        name
            Name of the new table.
        obj
            An Ibis table expression or pandas table that will be used to
            extract the schema and the data of the new table. If not provided,
            `schema` must be given.
        schema
            The schema for the new table. Only one of `schema` or `obj` can be
            provided.
        database
            Name of the database where the table will be created, if not the
            default.
        """
        raise NotImplementedError(
            f'Backend "{self.name}" does not implement "create_table"'
        )

    def drop_table(
        self,
        name: str,
        database: str | None = None,
        force: bool = False,
    ) -> None:
        """Drop a table.

        Parameters
        ----------
        name
            Name of the table to drop.
        database
            Name of the database where the table exists, if not the default.
        force
            If `False`, an exception is raised if the table does not exist.
        """
        raise NotImplementedError(
            f'Backend "{self.name}" does not implement "drop_table"'
        )

    def create_view(
        self,
        name: str,
        expr: ir.Table,
        database: str | None = None,
    ) -> None:
        """Create a view.

        Parameters
        ----------
        name
            Name for the new view.
        expr
            An Ibis table expression that will be used to extract the query
            of the view.
        database
            Name of the database where the view will be created, if not the
            default.
        """
        raise NotImplementedError(
            f'Backend "{self.name}" does not implement "create_view"'
        )

    def drop_view(
        self, name: str, database: str | None = None, force: bool = False
    ) -> None:
        """Drop a view.

        Parameters
        ----------
        name
            Name of the view to drop.
        database
            Name of the database where the view exists, if not the default.
        force
            If `False`, an exception is raised if the view does not exist.
        """
        raise NotImplementedError(
            f'Backend "{self.name}" does not implement "drop_view"'
        )

    @classmethod
    def has_operation(cls, operation: type[ops.Value]) -> bool:
        """Return whether the backend implements support for `operation`.

        Parameters
        ----------
        operation
            A class corresponding to an operation.

        Returns
        -------
        bool
            Whether the backend implements the operation.

        Examples
        --------
        >>> import ibis
        >>> import ibis.expr.operations as ops
        >>> ibis.sqlite.has_operation(ops.ArrayIndex)
        False
        >>> ibis.postgres.has_operation(ops.ArrayIndex)
        True
        """
        raise NotImplementedError(
            f"{cls.name} backend has not implemented `has_operation` API"
        )


@functools.lru_cache(maxsize=None)
def _get_backend_names() -> frozenset[str]:
    """Return the set of known backend names.

    Notes
    -----
    This function returns a frozenset to prevent cache pollution.

    If a `set` is used, then any in-place modifications to the set
    are visible to every caller of this function.
    """

    if sys.version_info < (3, 10):
        entrypoints = importlib.metadata.entry_points()["ibis.backends"]
    else:
        entrypoints = importlib.metadata.entry_points(group="ibis.backends")
    return frozenset(ep.name for ep in entrypoints)


def connect(resource: Path | str, **kwargs: Any) -> BaseBackend:
    """Connect to `resource`, inferring the backend automatically.

    Parameters
    ----------
    resource
        A URL or path to the resource to be connected to.
    kwargs
        Backend specific keyword arguments

    Examples
    --------
    Connect to an in-memory duckdb database:
    >>> con = ibis.connect("duckdb://")

    Connect to an on-disk sqlite database:
    >>> con = ibis.connect("sqlite://relative/path/to/data.db")
    >>> con = ibis.connect("sqlite:///absolute/path/to/data.db")

    Connect to a postgres server:
    >>> con = ibis.connect("postgres://user:password@hostname:5432")
    """
    url = resource = str(resource)

    if re.match("[A-Za-z]:", url):
        # windows path with drive, treat it as a file
        url = f"file://{url}"

    parsed = urllib.parse.urlparse(url)
    scheme = parsed.scheme or "file"

    # Merge explicit kwargs with query string, explicit kwargs
    # taking precedence
    kwargs = dict(urllib.parse.parse_qsl(parsed.query), **kwargs)

    if scheme == "file":
        path = parsed.netloc + parsed.path
        if path.endswith(".duckdb"):
            return ibis.duckdb.connect(path, **kwargs)
        elif path.endswith((".sqlite", ".db")):
            return ibis.sqlite.connect(path, **kwargs)
        elif path.endswith((".parquet", ".csv", ".csv.gz")):
            # Load parquet/csv/csv.gz files with duckdb by default
            con = ibis.duckdb.connect(**kwargs)
            con.register(path)
            return con
        else:
            raise ValueError(f"Don't know how to connect to {resource!r}")

    if kwargs:
        # If there are kwargs (either explicit or from the query string),
        # re-add them to the parsed URL
        query = urllib.parse.urlencode(kwargs)
        parsed = parsed._replace(query=query)

    if scheme in ("postgres", "postgresql"):
        # Treat `postgres://` and `postgresql://` the same, just as postgres
        # does. We normalize to `postgresql` since that's what SQLAlchemy
        # accepts.
        scheme = "postgres"
        parsed = parsed._replace(scheme="postgresql")

    # Convert all arguments back to a single URL string
    url = parsed.geturl()
    if "://" not in url:
        # SQLAlchemy requires a `://`, while urllib may roundtrip
        # `duckdb://` to `duckdb:`. Here we re-add the missing `//`.
        url = url.replace(":", "://", 1)
    if scheme in ("duckdb", "sqlite", "pyspark"):
        # SQLAlchemy wants an extra slash for URLs where the path
        # maps to a relative/absolute location on the filesystem
        url = url.replace(":", ":/", 1)

    try:
        backend = getattr(ibis, scheme)
    except AttributeError:
        raise ValueError(f"Don't know how to connect to {resource!r}") from None

    return backend._from_url(url)

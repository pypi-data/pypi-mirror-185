from typing import Any

import pandas as pd
import pandas.testing as tm
import pytest

import ibis
import ibis.common.exceptions as com
import ibis.expr.datatypes as dt
import ibis.expr.operations as ops
from ibis.backends.pandas import Backend
from ibis.backends.pandas.core import is_computable_input
from ibis.backends.pandas.dispatch import execute_node, post_execute, pre_execute
from ibis.backends.pandas.execution import execute
from ibis.expr.scope import Scope


@pytest.fixture
def dataframe():
    return pd.DataFrame(
        {
            'plain_int64': list(range(1, 4)),
            'plain_strings': list('abc'),
            'dup_strings': list('dad'),
        }
    )


@pytest.fixture
def core_client(dataframe):
    return Backend().connect({'df': dataframe})


@pytest.fixture
def ibis_table(core_client):
    return core_client.table('df')


def test_from_dataframe(dataframe, ibis_table, core_client):
    t = Backend().from_dataframe(dataframe)
    result = t.execute()
    expected = ibis_table.execute()
    tm.assert_frame_equal(result, expected)

    t = Backend().from_dataframe(dataframe, name='foo')
    expected = ibis_table.execute()
    tm.assert_frame_equal(result, expected)

    client = core_client
    t = Backend().from_dataframe(dataframe, name='foo', client=client)
    expected = ibis_table.execute()
    tm.assert_frame_equal(result, expected)


def test_pre_execute_basic():
    """Test that pre_execute has intercepted execution and provided its own
    scope dict."""

    @pre_execute.register(ops.Add)
    def pre_execute_test(op, *clients, scope=None, **kwargs):
        return Scope({op: 4}, None)

    one = ibis.literal(1)
    expr = one + one
    result = execute(expr.op())
    assert result == 4

    del pre_execute.funcs[(ops.Add,)]
    pre_execute.reorder()
    pre_execute._cache.clear()


def test_execute_parameter_only():
    param = ibis.param('int64')
    result = execute(param.op(), params={param.op(): 42})
    assert result == 42


def test_missing_data_sources():
    t = ibis.table([('a', 'string')])
    expr = t.a.length()
    with pytest.raises(com.UnboundExpressionError):
        execute(expr.op())


def test_missing_data_on_custom_client():
    class MyBackend(Backend):
        def table(self, name):
            return ops.DatabaseTable(
                name, ibis.schema([('a', 'int64')]), self
            ).to_expr()

    con = MyBackend()
    t = con.table('t')
    with pytest.raises(
        NotImplementedError,
        match=('Could not find signature for execute_node: <DatabaseTable, MyBackend>'),
    ):
        con.execute(t)


def test_post_execute_called_on_joins(dataframe, core_client, ibis_table):
    count = [0]

    @post_execute.register(ops.InnerJoin, pd.DataFrame)
    def tmp_left_join_exe(op, lhs, **kwargs):
        count[0] += 1
        return lhs

    left = ibis_table
    right = left.view()
    join = left.join(right, 'plain_strings')[left.plain_int64]
    result = join.execute()
    assert result is not None
    assert not result.empty
    assert count[0] == 1


def test_is_computable_input():
    class MyObject:
        def __init__(self, value: float) -> None:
            self.value = value

        def __getattr__(self, name: str) -> Any:
            return getattr(self.value, name)

        def __hash__(self) -> int:
            return hash((type(self), self.value))

        def __eq__(self, other):
            return (
                isinstance(other, type(self))
                and isinstance(self, type(other))
                and self.value == other.value
            )

        def __float__(self) -> float:
            return self.value

    @execute_node.register(ops.Add, int, MyObject)
    def add_int_my_object(op, left, right, **kwargs):
        return left + right.value

    # This multimethod must be implemented to play nicely with other value
    # types like columns and literals. In other words, for a custom
    # non-expression object to play nicely it must somehow map to one of the
    # types in ibis/expr/datatypes.py
    @dt.infer.register(MyObject)
    def infer_my_object(_, **kwargs):
        return dt.float64

    @is_computable_input.register(MyObject)
    def is_computable_input_my_object(_):
        return True

    one = ibis.literal(1)
    two = MyObject(2.0)
    assert is_computable_input(two)

    three = one + two
    four = three + 1
    result = execute(four.op())
    assert result == 4.0


def test_scope_look_up():
    # test if scope could lookup items properly
    scope = Scope()
    one_day = ibis.interval(days=1).op()
    one_hour = ibis.interval(hours=1).op()
    scope = scope.merge_scope(Scope({one_day: 1}, None))
    assert scope.get_value(one_hour) is None
    assert scope.get_value(one_day) is not None

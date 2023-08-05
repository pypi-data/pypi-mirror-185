from __future__ import annotations

import functools
import operator

import sqlalchemy as sa
import toolz
from multipledispatch import Dispatcher

import ibis
import ibis.common.exceptions as com
import ibis.expr.datatypes as dt
import ibis.expr.operations as ops
from ibis.backends.base.sql.alchemy import (
    fixed_arity,
    reduction,
    sqlalchemy_operation_registry,
    sqlalchemy_window_functions_registry,
    unary,
    varargs,
    variance_reduction,
)
from ibis.backends.base.sql.alchemy.datatypes import to_sqla_type
from ibis.backends.base.sql.alchemy.registry import _clip, _gen_string_find

operation_registry = sqlalchemy_operation_registry.copy()
operation_registry.update(sqlalchemy_window_functions_registry)


sqlite_cast = Dispatcher("sqlite_cast")


@sqlite_cast.register(object, dt.Integer, dt.Timestamp)
def _unixepoch(arg, from_, to):
    return sa.func.datetime(arg, "unixepoch")


@sqlite_cast.register(object, dt.String, dt.Timestamp)
def _string_to_timestamp(arg, from_, to):
    return sa.func.strftime('%Y-%m-%d %H:%M:%f', arg)


@sqlite_cast.register(object, dt.Integer, dt.Date)
def _integer_to_date(arg, from_, to):
    return sa.func.date(sa.func.datetime(arg, "unixepoch"))


@sqlite_cast.register(object, (dt.String, dt.Timestamp), dt.Date)
def _string_or_timestamp_to_date(arg, from_, to):
    return sa.func.date(arg)


@sqlite_cast.register(object, dt.DataType, (dt.Date, dt.Timestamp))
def _value_to_temporal(arg, from_, to):
    raise com.UnsupportedOperationError(type(arg))


@sqlite_cast.register(object, dt.Category, dt.Int32)
def _category_to_int(arg, from_, to):
    return arg


@sqlite_cast.register(object, dt.DataType, dt.DataType)
def _default_cast_impl(arg, from_, to):
    return sa.cast(arg, to_sqla_type(to))


def _strftime_int(fmt):
    def translator(t, op):
        # TODO(kszucs): avoid expr roundtrip, should be done in rewrite phase
        new_expr = op.arg.to_expr().strftime(fmt).cast(dt.int32)
        return t.translate(new_expr.op())

    return translator


def _extract_quarter(t, op):
    expr_new = ops.ExtractMonth(op.arg).to_expr()
    expr_new = (
        ibis.case()
        .when(expr_new.isin([1, 2, 3]), 1)
        .when(expr_new.isin([4, 5, 6]), 2)
        .when(expr_new.isin([7, 8, 9]), 3)
        .else_(4)
        .end()
    )
    return sa.cast(t.translate(expr_new.op()), sa.Integer)


_truncate_modifiers = {
    'Y': 'start of year',
    'M': 'start of month',
    'D': 'start of day',
    'W': 'weekday 1',
}


def _truncate(func):
    def translator(t, op):
        sa_arg = t.translate(op.arg)
        try:
            modifier = _truncate_modifiers[op.unit]
        except KeyError:
            raise com.UnsupportedOperationError(
                f'Unsupported truncate unit {op.unit!r}'
            )
        return func(sa_arg, modifier)

    return translator


def _log(t, op):
    sa_arg = t.translate(op.arg)
    if op.base is None:
        return sa.func._ibis_sqlite_ln(sa_arg)
    return sa.func._ibis_sqlite_log(sa_arg, t.translate(op.base))


def _generic_pad(arg, length, pad):
    f = sa.func
    arg_length = f.length(arg)
    pad_length = f.length(pad)
    number_of_zero_bytes = ((length - arg_length - 1 + pad_length) / pad_length + 1) / 2
    return f.substr(
        f.replace(
            f.replace(f.substr(f.quote(f.zeroblob(number_of_zero_bytes)), 3), "'", ''),
            '0',
            pad,
        ),
        1,
        length - f.length(arg),
    )


def _extract_week_of_year(t, op):
    """ISO week of year.

    This solution is based on https://stackoverflow.com/a/15511864 and handle
    the edge cases when computing ISO week from non-ISO week.

    The implementation gives the same results as `datetime.isocalendar()`.

    The year's week that "wins" the day is the year with more alloted days.

    For example:

    ```
    $ cal '2011-01-01'
        January 2011
    Su Mo Tu We Th Fr Sa
                      |1|
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 31
    ```

    Here the ISO week number is `52` since the day occurs in a week with more
    days in the week occuring in the _previous_ week's year.

    ```
    $ cal '2012-12-31'
        December 2012
    Su Mo Tu We Th Fr Sa
                       1
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 |31|
    ```

    Here the ISO week of year is `1` since the day occurs in a week with more
    days in the week occuring in the _next_ week's year.
    """
    date = sa.func.date(t.translate(op.arg), "-3 days", "weekday 4")
    return (sa.func.strftime("%j", date) - 1) / 7 + 1


def _string_join(t, op):
    return functools.reduce(
        operator.add,
        toolz.interpose(t.translate(op.sep), map(t.translate, op.arg)),
    )


operation_registry.update(
    {
        # TODO(kszucs): don't dispatch on op.arg since that should be always an
        # instance of ops.Value
        ops.Cast: (
            lambda t, op: sqlite_cast(t.translate(op.arg), op.arg.output_dtype, op.to)
        ),
        ops.StrRight: fixed_arity(
            lambda arg, nchars: sa.func.substr(arg, -nchars, nchars), 2
        ),
        ops.StringFind: _gen_string_find(sa.func.instr),
        ops.StringJoin: _string_join,
        ops.StringConcat: (
            lambda t, op: functools.reduce(operator.add, map(t.translate, op.arg))
        ),
        ops.Least: varargs(sa.func.min),
        ops.Greatest: varargs(sa.func.max),
        ops.IfNull: fixed_arity(sa.func.ifnull, 2),
        ops.DateFromYMD: fixed_arity(
            lambda y, m, d: sa.func.date(sa.func.printf('%04d-%02d-%02d', y, m, d)), 3
        ),
        ops.TimeFromHMS: fixed_arity(
            lambda h, m, s: sa.func.time(sa.func.printf('%02d:%02d:%02d', h, m, s)), 3
        ),
        ops.TimestampFromYMDHMS: fixed_arity(
            lambda y, mo, d, h, m, s: sa.func.datetime(
                sa.func.printf('%04d-%02d-%02d %02d:%02d:%02d%s', y, mo, d, h, m, s)
            ),
            6,
        ),
        ops.DateTruncate: _truncate(sa.func.date),
        ops.Date: unary(sa.func.date),
        ops.Time: unary(sa.func.time),
        ops.TimestampTruncate: _truncate(sa.func.datetime),
        ops.Strftime: fixed_arity(
            lambda arg, format_str: sa.func.strftime(format_str, arg), 2
        ),
        ops.ExtractYear: _strftime_int('%Y'),
        ops.ExtractMonth: _strftime_int('%m'),
        ops.ExtractDay: _strftime_int('%d'),
        ops.ExtractWeekOfYear: _extract_week_of_year,
        ops.ExtractDayOfYear: _strftime_int('%j'),
        ops.ExtractQuarter: _extract_quarter,
        # example: (julianday('now') - 2440587.5) * 86400.0
        ops.ExtractEpochSeconds: fixed_arity(
            lambda arg: sa.cast(
                (sa.func.julianday(arg) - 2440587.5) * 86400.0, sa.BigInteger
            ),
            1,
        ),
        ops.ExtractHour: _strftime_int('%H'),
        ops.ExtractMinute: _strftime_int('%M'),
        ops.ExtractSecond: _strftime_int('%S'),
        ops.ExtractMillisecond: fixed_arity(
            lambda arg: (sa.func.strftime('%f', arg) * 1000) % 1000, 1
        ),
        ops.TimestampNow: fixed_arity(lambda: sa.func.datetime("now"), 0),
        ops.RegexSearch: fixed_arity(sa.func._ibis_sqlite_regex_search, 2),
        ops.RegexReplace: fixed_arity(sa.func._ibis_sqlite_regex_replace, 3),
        ops.RegexExtract: fixed_arity(sa.func._ibis_sqlite_regex_extract, 3),
        ops.LPad: fixed_arity(
            lambda arg, length, pad: _generic_pad(arg, length, pad) + arg, 3
        ),
        ops.RPad: fixed_arity(
            lambda arg, length, pad: arg + _generic_pad(arg, length, pad), 3
        ),
        ops.Repeat: fixed_arity(
            lambda arg, times: sa.func.replace(
                sa.func.substr(
                    sa.func.quote(sa.func.zeroblob((times + 1) / 2)), 3, times
                ),
                '0',
                arg,
            ),
            2,
        ),
        ops.Reverse: unary(sa.func._ibis_sqlite_reverse),
        ops.StringAscii: unary(sa.func._ibis_sqlite_string_ascii),
        ops.Capitalize: unary(sa.func._ibis_sqlite_capitalize),
        ops.Translate: fixed_arity(sa.func._ibis_sqlite_translate, 3),
        ops.Sqrt: unary(sa.func._ibis_sqlite_sqrt),
        ops.Power: fixed_arity(sa.func._ibis_sqlite_power, 2),
        ops.Exp: unary(sa.func._ibis_sqlite_exp),
        ops.Ln: unary(sa.func._ibis_sqlite_ln),
        ops.Log: _log,
        ops.Log10: unary(sa.func._ibis_sqlite_log10),
        ops.Log2: unary(sa.func._ibis_sqlite_log2),
        ops.Floor: unary(sa.func._ibis_sqlite_floor),
        ops.Ceil: unary(sa.func._ibis_sqlite_ceil),
        ops.Sign: unary(sa.func._ibis_sqlite_sign),
        ops.FloorDivide: fixed_arity(sa.func._ibis_sqlite_floordiv, 2),
        ops.Modulus: fixed_arity(sa.func._ibis_sqlite_mod, 2),
        ops.Variance: variance_reduction('_ibis_sqlite_var'),
        ops.StandardDev: toolz.compose(
            sa.func._ibis_sqlite_sqrt, variance_reduction('_ibis_sqlite_var')
        ),
        ops.RowID: lambda *_: sa.literal_column('rowid'),
        ops.Cot: unary(sa.func._ibis_sqlite_cot),
        ops.Cos: unary(sa.func._ibis_sqlite_cos),
        ops.Sin: unary(sa.func._ibis_sqlite_sin),
        ops.Tan: unary(sa.func._ibis_sqlite_tan),
        ops.Acos: unary(sa.func._ibis_sqlite_acos),
        ops.Asin: unary(sa.func._ibis_sqlite_asin),
        ops.Atan: unary(sa.func._ibis_sqlite_atan),
        ops.Atan2: fixed_arity(sa.func._ibis_sqlite_atan2, 2),
        ops.BitOr: reduction(sa.func._ibis_sqlite_bit_or),
        ops.BitAnd: reduction(sa.func._ibis_sqlite_bit_and),
        ops.BitXor: reduction(sa.func._ibis_sqlite_bit_xor),
        ops.Degrees: unary(sa.func._ibis_sqlite_degrees),
        ops.Radians: unary(sa.func._ibis_sqlite_radians),
        ops.Clip: _clip(min_func=sa.func.min, max_func=sa.func.max),
        # sqlite doesn't implement a native xor operator
        ops.BitwiseXor: fixed_arity(sa.func._ibis_sqlite_xor, 2),
        ops.BitwiseNot: unary(sa.func._ibis_sqlite_inv),
        ops.Where: fixed_arity(sa.func.iif, 3),
        ops.Pi: fixed_arity(sa.func._ibis_sqlite_pi, 0),
        ops.E: fixed_arity(sa.func._ibis_sqlite_e, 0),
    }
)

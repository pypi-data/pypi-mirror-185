WITH t0 AS (
  SELECT *, `b` * 2 AS `b2`
  FROM my_table
),
t1 AS (
  SELECT t0.`a`, t0.`b2`
  FROM t0
  WHERE t0.`a` < 100
)
SELECT t1.*
FROM t1
WHERE t1.`a` = (
  SELECT max(`a`) AS `blah`
  FROM t1
)
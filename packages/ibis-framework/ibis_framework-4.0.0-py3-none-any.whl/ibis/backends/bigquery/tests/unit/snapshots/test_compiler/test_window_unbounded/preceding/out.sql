SELECT sum(`a`) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS `tmp`
FROM t
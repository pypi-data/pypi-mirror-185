SELECT sum(`d`) OVER (ORDER BY `f` ASC ROWS BETWEEN 10 PRECEDING AND 5 PRECEDING) AS `foo`
FROM alltypes
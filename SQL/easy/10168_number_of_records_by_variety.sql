-- 10168 number of records by variety
SELECT variety, COUNT(*) AS n_total_varieties
FROM iris
GROUP BY variety;
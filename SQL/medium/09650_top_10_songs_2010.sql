-- 9650 top 10 songs 2010
SELECT DISTINCT song_name, year_rank, group_name
FROM billboard_top_100_year_end
WHERE year = 2010
ORDER BY year_rank ASC
LIMIT 10;
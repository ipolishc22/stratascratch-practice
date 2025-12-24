-- 9999 find songsd that are ranked between 8-10
SELECT trackname, position
FROM spotify_worldwide_daily_song_ranking
WHERE position < 11 AND position > 7
ORDER BY position ASC;
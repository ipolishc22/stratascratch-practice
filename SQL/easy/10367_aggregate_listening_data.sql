-- 10367 aggregate listening data
SELECT user_id, ROUND(SUM(listen_duration)/60, 0) AS total_listen_duration, COUNT(DISTINCT song_id) AS unique_song_count
FROM listening_habits
GROUP BY user_id;
-- 10539 user activity count
SELECT u.user_id, COUNT(DISTINCT a.activity_type) AS total_unique_activities
FROM user_profiles u
LEFT JOIN activity_log a ON u.user_id = a.user_id
GROUP BY user_id;
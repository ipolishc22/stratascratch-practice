-- 2126 account registration
SELECT DATE_FORMAT(started_at, '%Y-%m') AS started_month, COUNT(signup_id) AS n_registrations
FROM noom_signups
GROUP BY started_month;
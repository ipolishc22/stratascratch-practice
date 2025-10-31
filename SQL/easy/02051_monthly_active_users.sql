-- 2051 Monthly Active Users
SELECT account_id, COUNT(DISTINCT user_id) AS user_count
FROM sf_events
WHERE record_date BETWEEN '2021-01-01' AND '2021-01-30'
GROUP BY account_id;
-- 2017 Paid Users in April 2020
SELECT COUNT(DISTINCT rc_users.user_id) AS count
FROM rc_users
JOIN rc_calls ON rc_calls.user_id = rc_users.user_id
WHERE call_date BETWEEN '2020-04-01' AND '2020-04-30' AND status = 'paid' ;
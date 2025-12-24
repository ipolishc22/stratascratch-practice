-- 10061 popularity of hack
SELECT e.location, AVG(s.popularity)
FROM facebook_employees e
LEFT JOIN facebook_hack_survey s ON s.employee_id = e.id
GROUP BY e.location;
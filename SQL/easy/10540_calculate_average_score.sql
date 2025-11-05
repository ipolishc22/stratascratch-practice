-- 10540 calculate average score
SELECT project_id, AVG(score) AS avg_score
FROM project_data
GROUP BY project_id
HAVING COUNT(team_member_id) > 1;
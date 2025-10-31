-- 2083 Pending Clamims 
SELECT COUNT(DISTINCT account_id) AS count
FROM cvs_claims
WHERE date_accepted IS NULL AND date_rejected IS NULL;
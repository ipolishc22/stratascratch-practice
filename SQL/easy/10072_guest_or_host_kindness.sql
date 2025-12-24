-- 10072 guest or host kindness
SELECT from_type, ROUND(AVG(review_score), 2) AS avg_review_score
FROM airbnb_reviews
GROUP BY from_type
ORDER BY avg_review_score DESC
LIMIT 1;
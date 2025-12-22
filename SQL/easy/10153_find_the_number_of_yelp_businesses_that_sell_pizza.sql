-- 10153 find the number of yelp businesses that sell pizza
SELECT COUNT(business_id)
FROM yelp_business
WHERE categories LIKE '%Pizza%';
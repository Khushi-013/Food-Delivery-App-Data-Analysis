#write your query
SELECT
    type,
    COUNT(*) AS number_of_restaurants,
    SUM(votes) AS total_votes,
    AVG(rating) AS avg_rating
FROM
    zomato
WHERE
    type IS NOT NULL
    AND type NOT IN ('NULL', 'N/A', 'NA') -- add other non-null values to exclude
GROUP BY
    type
ORDER BY
    total_votes DESC;

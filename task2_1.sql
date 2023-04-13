#write your query
SELECT name, votes, rating
FROM zomato
WHERE type = 'Delivery'
ORDER BY votes DESC
LIMIT 5;

#write your query
SELECT name, rating, votes, online_order
FROM zomato
WHERE votes >= 150
AND rating > 3
AND online_order = 'No'
ORDER BY votes DESC
LIMIT 15;

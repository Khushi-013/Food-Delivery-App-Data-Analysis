#write your query
SELECT 
    SUM(votes) AS total_votes, 
    online_order 
FROM 
    zomato 
GROUP BY 
    online_order;

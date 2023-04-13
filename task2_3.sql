#write your query
SELECT (SELECT rating FROM zomato WHERE location = "Indiranagar" ORDER BY approx_cost ASC LIMIT 1) AS cheapest_rating, 
       (SELECT rating FROM zomato WHERE location = "Indiranagar" ORDER BY approx_cost DESC LIMIT 1) AS expensive_rating;

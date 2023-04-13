SELECT (SELECT rating from zomato where location "Indiranagar" order by approx_cost ASC limit 1) as rating, rating
FROM zomato
WHERE location = 'Indiranagar'
ORDER BY approx_cost DESC
LIMIT 1;

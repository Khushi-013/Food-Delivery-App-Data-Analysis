SELECT name, dish_liked, rating, votes
FROM zomato
WHERE votes=(SELECT MAX(votes) FROM zomato);

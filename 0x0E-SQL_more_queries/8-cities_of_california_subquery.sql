-- lists all the cities of california that can be founD
SELECT id, name FROM cities
WHERE state_id = 
	(SELECT id FROM states
		WHERE name = 'California');

-- lists all the cities of california that can be founD
SELECT name FROM hbtn_0d_usa.cities
WHERE state_id = 
	(SELECT id FROM hbtn_0d_usa.states
		WHERE name = 'California');

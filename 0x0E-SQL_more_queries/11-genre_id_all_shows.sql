--lists all shows in the database
SELECT s.title, g.genre_id
	FROM tv_shows AS s, tv_show_genres AS g
	WHERE s.id = g.show_id
	ORDER BY s.title, g.genre_id;

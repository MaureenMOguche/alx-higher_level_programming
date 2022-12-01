--lists all shows in the database
SELECT s.title, g.genre_id
	FROM tv_shows AS s
		LEFT JOIN tv_show_genres AS g
		ON s.id = g.show_id
	ORDER BY tv_shows.title, tv_show_genres.genre_id

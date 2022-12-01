--lists all shows in the database
SELECT s.title, g.genre_id
FROM tv_shows AS s, tv_show_genres AS g
WHERE tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id

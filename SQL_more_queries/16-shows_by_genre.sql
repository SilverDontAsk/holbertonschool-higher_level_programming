-- lists all shows and their genres
SELECT s.title AS title, g.name AS name
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN tv_genres g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;

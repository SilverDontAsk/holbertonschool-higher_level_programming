-- lists all genres from hbtn_0d_tvshows then displays the number of shows linked to it
SELECT g.name AS genre, COUNT(s.id) AS number_of_shows
FROM tv_genres g
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id
LEFT JOIN tv_shows s ON sg.show_id = s.id
GROUP BY g.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

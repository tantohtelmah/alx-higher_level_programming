-- list all shows from database by their rating
SELECT tv_shows.title, SUM(hbtn_0d_tvshows_rate.rating) AS rating_sum
FROM tv_shows
JOIN hbtn_0d_tvshows_rate ON shows.id = hbtn_0d_tvshows_rate.show_id
GROUP BY shows.id
ORDER BY rating_sum DESC;

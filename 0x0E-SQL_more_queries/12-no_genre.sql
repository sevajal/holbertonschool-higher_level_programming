-- Script that lists all shows contained in hbtn_0d_tvshows without a genre linked. 
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT OUTER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.id IS NULL AND tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

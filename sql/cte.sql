WITH cte_artist
AS (
	SELECT t1.artist
		,count(*) AS qtd_artist
	FROM PUBLIC."Billboard1" AS t1
	GROUP BY t1.artist
	ORDER BY t1.artist
	)
	,cte_song
AS (
	SELECT t1.song
		,count(*) AS qtd_song
	FROM PUBLIC."Billboard1" AS t1
	GROUP BY t1.song
	ORDER BY t1.song
	)
SELECT t1.artist
	,t2.qtd_artist
	,t1.song
	,t3.qtd_song
FROM PUBLIC."Billboard1" AS t1
LEFT JOIN cte_artist AS t2 ON (t1.artist = t2.artist)
LEFT JOIN cte_song AS t3 ON (t1.song = t3.song);
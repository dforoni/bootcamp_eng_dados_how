WITH CTE_BILLBOARD
AS (
	SELECT DISTINCT t1.artist
		,t1.song
	FROM PUBLIC."Billboard" AS t1
	ORDER BY t1.artist
		,t1.song
	)
SELECT *
	,row_number() OVER (
		ORDER BY artist
			,song
		) AS "row_number"
	,row_number() OVER (
		PARTITION BY artist ORDER BY artist
			,song
		) AS "row_number_by_artist"
	,rank() OVER (
		PARTITION BY artist ORDER BY artist
			,song
		) AS "rank_artist"
	,lag(song, 1) OVER (
		ORDER BY artist
			,song
		) AS "lag_song"
	,lead(song, 1) OVER (
		ORDER BY artist
			,song
		) AS "lead_song"
	,first_value(song) OVER (
		PARTITION BY artist ORDER BY artist
			,song
		) AS "first_song"
	,last_value(song) OVER (
		PARTITION BY artist ORDER BY artist
			,song RANGE BETWEEN UNBOUNDED PRECEDING
				AND UNBOUNDED FOLLOWING
		) AS "last_song"
	,nth_value(song, 2) OVER (
		PARTITION BY artist ORDER BY artist
			,song
		) AS "nth_song"
FROM CTE_BILLBOARD
-- Exemplo geral
WITH T (
	StyleID
	,ID
	,Nome
	)
AS (
	SELECT 1 ,1 ,'Rhuan'
	
	UNION ALL
	
	SELECT 1 ,1 ,'Andre'
	
	UNION ALL
	
	SELECT 1 ,2 ,'Ana'
	
	UNION ALL
	
	SELECT 1 ,2	,'Maria'
	
	UNION ALL
	
	SELECT 1 ,3 ,'Let?cia'
	
	UNION ALL
	
	SELECT 1 ,3	,'Lari'
	
	UNION ALL
	
	SELECT 1 ,4	,'Edson'
	
	UNION ALL
	
	SELECT 1 ,4	,'Marcos'
	
	UNION ALL
	
	SELECT 1 ,5 ,'Rhuan'
	
	UNION ALL
	
	SELECT 1 ,5	,'Lari'
	
	UNION ALL
	
	SELECT 1 ,6	,'Daisy'
	
	UNION ALL
	
	SELECT 1 ,6	,'Jo?o'
	)
SELECT *
	,ROW_NUMBER() OVER (PARTITION BY StyleID ORDER BY ID) AS "ROW_NUMBER"
	,RANK() OVER (PARTITION BY StyleID ORDER BY ID) AS "RANK"
	,DENSE_RANK() OVER (PARTITION BY StyleID ORDER BY ID) AS "DENSE_RANK"
	,PERCENT_RANK() OVER (PARTITION BY StyleID ORDER BY ID) AS "PERCENT_RANK"
	,CUME_DIST() OVER (PARTITION BY StyleID ORDER BY ID) AS "CUME_DIST"
	,CUME_DIST() OVER (PARTITION BY StyleID ORDER BY ID DESC) AS "CUME_DIST_DESC"
	,FIRST_VALUE(Nome) OVER (PARTITION BY StyleID ORDER BY ID) AS "FIRST_VALUE"
	,LAST_VALUE(Nome) OVER (PARTITION BY StyleID ORDER BY ID) AS "LAST_VALUE"
	,NTH_VALUE(Nome, 5) OVER (PARTITION BY StyleID ORDER BY ID) AS "NTH_VALUE"
	,NTILE(5) OVER (ORDER BY StyleID) AS "NTILE_5"
	,LAG(Nome, 1) OVER (ORDER BY ID) AS "LAG_NOME"
	,LEAD(Nome, 1) OVER (ORDER BY ID) AS "LEAD_NOME"
FROM T
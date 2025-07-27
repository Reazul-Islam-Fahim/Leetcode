-- postgresql, oracle, mssql

SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;


-- mysql

SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;

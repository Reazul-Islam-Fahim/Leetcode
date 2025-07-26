-- mysql, mssql and postgresql

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;


-- oracle

SELECT 
  player_id, 
  TO_CHAR(MIN(event_date), 'YYYY-MM-DD') AS first_login
FROM Activity
GROUP BY player_id;

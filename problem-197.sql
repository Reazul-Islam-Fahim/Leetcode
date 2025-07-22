-- mysql

SELECT W1.id
FROM Weather W1
JOIN Weather W2
  ON DATEDIFF(W1.recordDate, W2.recordDate) = 1
WHERE W1.temperature > W2.temperature;



-- postgresql

SELECT W1.id
FROM Weather W1
JOIN Weather W2
  ON W1.recordDate = W2.recordDate + INTERVAL '1 day'
WHERE W1.temperature > W2.temperature;


-- oracle

SELECT W1.id
FROM Weather W1
JOIN Weather W2
  ON W1.recordDate = W2.recordDate + 1
WHERE W1.temperature > W2.temperature;


--  mssql

SELECT W1.id
FROM Weather W1
JOIN Weather W2
  ON W1.recordDate = DATEADD(day, 1, W2.recordDate)
WHERE W1.temperature > W2.temperature;

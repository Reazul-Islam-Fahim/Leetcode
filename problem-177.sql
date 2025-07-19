--mysql

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
    SELECT DISTINCT salary
    FROM (
      SELECT
        salary,
        DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
      FROM Employee
    ) AS ranked_salaries
    WHERE rnk = N
  );
END



--mssql

CREATE FUNCTION getNthHighestSalary(@N INT)
RETURNS INT
AS
BEGIN
    DECLARE @result INT;

    SELECT @result = salary
    FROM (
        SELECT
            salary,
            DENSE_RANK() OVER (ORDER BY salary DESC) as rnk
        FROM Employee
    ) AS ranked_salaries
    WHERE rnk = @N; 

    RETURN @result;
END;


--postgres

CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    SELECT DISTINCT s.salary 
    FROM (
      SELECT
        e.salary,
        DENSE_RANK() OVER (ORDER BY e.salary DESC) as rnk
      FROM Employee AS e
    ) AS s
    WHERE s.rnk = N
  );
END;
$$ LANGUAGE plpgsql;






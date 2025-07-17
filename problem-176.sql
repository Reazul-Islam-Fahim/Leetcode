-- mysql and postgesql

SELECT 
    (
        SELECT DISTINCT salary
        FROM Employee
        ORDER BY salary DESC
        LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary;


-- mssql

SELECT 
    CASE 
        WHEN COUNT(DISTINCT salary) < 2 THEN NULL
        ELSE (
            SELECT MAX(salary) 
            FROM Employee
            WHERE salary < (SELECT MAX(salary) FROM Employee)
        )
    END AS SecondHighestSalary
FROM Employee;


-- oracle

SELECT 
    CASE 
        WHEN distinct_count < 2 THEN NULL
        ELSE (
            SELECT MAX(salary) 
            FROM Employee
            WHERE salary < (SELECT MAX(salary) FROM Employee)
        )
    END AS SecondHighestSalary
FROM (
    SELECT COUNT(DISTINCT salary) AS distinct_count FROM Employee
);

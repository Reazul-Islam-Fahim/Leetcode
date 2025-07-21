--mysql and mssql

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email AND p1.id > p2.id;


--postgres

WITH UniqueEmails AS (
    SELECT MIN(id) AS id
    FROM Person
    GROUP BY email
)
DELETE FROM Person
WHERE id NOT IN (SELECT id FROM UniqueEmails);


--oracle

DELETE FROM Person
WHERE id NOT IN (
    SELECT MIN(id)
    FROM Person
    GROUP BY email
);

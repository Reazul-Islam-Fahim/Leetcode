WITH filtered AS (
    SELECT *, id - ROW_NUMBER() OVER (ORDER BY id) AS grp_id
    FROM Stadium
    WHERE people >= 100
),
valid_groups AS (
    SELECT grp_id
    FROM filtered
    GROUP BY grp_id
    HAVING COUNT(*) >= 3
)
SELECT f.id, f.visit_date, f.people
FROM filtered f
JOIN valid_groups vg ON f.grp_id = vg.grp_id
ORDER BY f.visit_date ASC;

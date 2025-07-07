WITH unbanned_clients AS (
    SELECT users_id FROM Users WHERE banned = 'No' AND role = 'client'
),
unbanned_drivers AS (
    SELECT users_id FROM Users WHERE banned = 'No' AND role = 'driver'
),
filtered_trips AS (
    SELECT id, client_id, driver_id, status, request_at::date AS day
    FROM Trips
    WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
      AND client_id IN (SELECT users_id FROM unbanned_clients)
      AND driver_id IN (SELECT users_id FROM unbanned_drivers)
)
SELECT
    day AS "Day",
    ROUND(
        SUM(CASE WHEN status IN ('cancelled_by_client', 'cancelled_by_driver') THEN 1 ELSE 0 END)::numeric
        / COUNT(*), 2
    ) AS "Cancellation Rate"
FROM filtered_trips
GROUP BY day
ORDER BY day;

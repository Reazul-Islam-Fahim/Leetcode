SELECT 
    product_id, 
    year AS first_year, 
    quantity, 
    price
FROM (
    SELECT 
        *,
        MIN(year) OVER (PARTITION BY product_id) AS first_year_per_product
    FROM Sales
) sub
WHERE year = first_year_per_product;

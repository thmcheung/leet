WITH red_salespersons AS (
    SELECT DISTINCT Orders.sales_id
    FROM Orders
    LEFT JOIN Company ON Orders.com_id = Company.com_id
    WHERE Company.name = 'RED'
)
SELECT Salesperson.name
FROM Salesperson
WHERE Salesperson.sales_id NOT IN (SELECT sales_id FROM red_salespersons);
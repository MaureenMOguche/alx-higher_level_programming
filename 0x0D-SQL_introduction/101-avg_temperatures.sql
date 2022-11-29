-- displays average temperature by city
SELECT city, AVG(value) AS avg_temp
GROUP BY city ORDER BY avg_temp DESC;

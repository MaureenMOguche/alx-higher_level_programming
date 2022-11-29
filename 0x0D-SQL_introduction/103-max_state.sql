-- display max temp of each state orderd by state
SELECT state, MAX(value) as max_temp FROM temperatures
GROUP BY state ORDER BY state;

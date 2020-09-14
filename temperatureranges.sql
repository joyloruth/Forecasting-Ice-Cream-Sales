SELECT revenue, ROUND(AVG(fahrenheit)) as Degree, Count(*) AS number_of_orders,
CASE 
WHEN ROUND(fahrenheit) BETWEEN 30 AND 39 THEN "30's"
WHEN ROUND(fahrenheit) BETWEEN 40 AND 49 THEN "40's"
WHEN ROUND(fahrenheit) BETWEEN 50 AND 59 THEN "50's"
WHEN ROUND(fahrenheit) BETWEEN 60 AND 69 THEN "60's"
WHEN ROUND(fahrenheit) BETWEEN 70 AND 79 THEN "70's"
WHEN ROUND(fahrenheit) BETWEEN 80 AND 89 THEN "80's"
WHEN ROUND(fahrenheit) BETWEEN 90 AND 99 THEN "90's"
WHEN ROUND(fahrenheit) BETWEEN 100 AND 109 THEN "100's"
WHEN ROUND(fahrenheit) BETWEEN 110 AND 119 THEN "110's"
END AS 'Degree Ranges'
FROM ice_cream_shop_sales
GROUP BY 4;

# 55	35	5	30's
# 238	46	31	40's
# 316	55	65	50's
# 488	65	109	60's
# 535	75	136	70's
# 661	84	100	80's
# 810	94	38	90's
# 905	104	15	100's
# 1000	113	1	110's

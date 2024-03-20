-- alx give me table and want me to minubultaion it
SELECT origin, sum(fans) as nb_fans
FROM metal_bands 
GROUP BY origin 
ORDER BY nb_fans DESC;

-- 10170 gender with the most doctor appointments
SELECT gender, COUNT(appointmentid) AS num_appointments 
FROM medical_appointments
GROUP BY gender
ORDER BY num_appointments DESC
LIMIT 1;
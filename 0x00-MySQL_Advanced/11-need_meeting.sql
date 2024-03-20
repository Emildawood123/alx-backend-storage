-- create my first view
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE Score > 80 
AND (last_meeting IS NULL 
OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH))
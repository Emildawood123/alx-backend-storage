-- create my first funcation in sql
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
BEGIN
    IF b = 0
        THEN RETURN 0;
    END IF;
    RETURN a / b; 
END $$
DELIMITER ;

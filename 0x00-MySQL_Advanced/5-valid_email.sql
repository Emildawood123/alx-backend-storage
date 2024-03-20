-- mhgms
CREATE TRIGGER trigger
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.email = 0
    END IF;
END;

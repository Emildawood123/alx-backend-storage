-- create trigger increase item when make order
CREATE TRIGGER decrease
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;

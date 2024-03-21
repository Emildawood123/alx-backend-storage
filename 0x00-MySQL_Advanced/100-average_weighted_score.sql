-- create procedure to compute weighted avaerage score
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN sec_user_id INT)
BEGIN
    new = sum(weighted) FROM projects WHERE user_id = sec_user_id;
    FOR EACH ROW UPDATE users
        SET average_score = average_score + ((score FROM corrections 
        WHERE user_id = sec_user_id * weighted 
        FROM projects WHERE user_id = sec_user_id) / new)
        WHERE id = sec_user_id;
END $$
DELIMITER ;
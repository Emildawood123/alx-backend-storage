-- procedure for compute Average Score for user
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN sec_user_id INT)
BEGIN
    UPDATE users
    SET average_score = SELECT AVG(score) FROM corrections WHERE user_id = sec_user_id
    WHERE id = sec_user_id
END $$
DELIMITER ;

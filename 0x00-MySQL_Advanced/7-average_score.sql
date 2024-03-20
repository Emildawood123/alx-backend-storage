-- procedure for compute Average Score for user
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN sec_user_id INT)
BEGIN
    DECLARE A = 0
    DECLARE B = 0
    FOR EACH ROW IN corrections
        A = A + corrections.score
        B = B + 1
        WHERE user_id = sec_user_id
    UPDATE users
    SET average_score = A / B
    WHERE id = sec_user_id
END $$
DELIMITER ;

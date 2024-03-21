-- creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id_param INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;
    SET total_weighted_score = 0;
    SET total_weight = 0;
    SELECT 
        SUM(corrections.score * projects.weight) AS total_weighted_score,
        SUM(projects.weight) AS total_weight
    INTO 
        total_weighted_score, total_weight
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id
    WHERE corrections.user_id = user_id_param;
    UPDATE users
    SET average_score = total_weighted_score / total_weight
    WHERE id = user_id_param;
END $$

DELIMITER ;

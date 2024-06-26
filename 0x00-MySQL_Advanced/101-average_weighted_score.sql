-- create procedure to compute average weight
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users
    SET average_score = (
        SELECT 
            IFNULL(SUM(corrections.score * projects.weight) / SUM(projects.weight), 0)
        FROM 
            corrections
        JOIN 
            projects ON projects.id = corrections.project_id
        WHERE 
            corrections.user_id = users.id);
END $$

DELIMITER ;

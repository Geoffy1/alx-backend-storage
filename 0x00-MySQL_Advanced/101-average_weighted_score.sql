-- computes and stores the average weighted score for all students:
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;
    DECLARE avg_weighted_score FLOAT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET total_weighted_score = 0;
        SET total_weight = 0;
        SELECT SUM(score * weight) INTO total_weighted_score, SUM(weight) INTO total_weight
        FROM corrections
        WHERE user_id = cur.user_id;
        IF total_weight IS NOT NULL AND total_weight != 0 THEN
            SET avg_weighted_score = total_weighted_score / total_weight;
            INSERT INTO average_weighted_scores (user_id, score) VALUES (cur.user_id, avg_weighted_score)
            ON DUPLICATE KEY UPDATE score = avg_weighted_score;
        END IF;
    END LOOP;

    CLOSE cur;
END$$
DELIMITER ;

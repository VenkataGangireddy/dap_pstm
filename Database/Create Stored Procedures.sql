-- Procedure to Get Topics
DELIMITER $$
CREATE DEFINER=`dapproject`@`%` PROCEDURE `Get_Topics`()
BEGIN
SELECT a.topic_id,a.Name, b.Topic_Entity_Id,b.Entity_Type,b.Entity_Value 
	FROM topics_tbl a, topic_entities_tbl b 
	WHERE a.topic_id = b.topic_id 
	AND a.Active_flag=1 
	AND b.Active_flag=1;
END$$
DELIMITER ;


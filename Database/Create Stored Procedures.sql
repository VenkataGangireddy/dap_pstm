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

-- Procedure to Create Event Logs
DELIMITER $$
CREATE DEFINER=`dapproject`@`%` PROCEDURE `Create_Event_Log`(p_Topic_Entity_Id INT,
                                                             p_Start_Time TIMESTAMP,
                                                             p_End_Time  TIMESTAMP,
                                                             p_Records_Processed INT,
                                                             p_status  VARCHAR(10))
BEGIN
INSERT INTO events_log_tbl (Topic_Entity_Id,
                            Start_Time,
                            End_Time,
                            Records_Processed,
                            status)
                   VALUES  (p_Topic_Entity_Id,
                            p_Start_Time,
                            p_End_Time,
                            p_Records_Processed,
                            p_status);
COMMIT;                          
END$$
DELIMITER ;

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
DELIMITER;

-- Stored Procedure to Get Tweets and Sentiments
DELIMITER $$
CREATE DEFINER=`dapproject`@`%` PROCEDURE `Get_Tweets_Sentiments`(tweet_type varchar(20))
BEGIN
	IF tweet_type = 'ORIGINAL' THEN
		SELECT a.Topic_Entity_Id as TopicID, a.Entity_Value as TopicName, b.Text as TweetMsg, b.Tweet_Date as TweetTimestamp, b.User_Screen_Name as TweetHandle, 
			   b.Tweet_Id as TweetID, c.Sentiment_Type as SentimentType, c.Sentiment_Percentage as SentimentPercent 
		FROM   topic_entities_tbl a,   
			   twitter_data_tbl b, 
			   twitter_sentiments_tbl c
		WHERE  a.Topic_Entity_Id = b.Topic_Entity_Id
		AND    b.Tweet_Id = c.Tweet_Id
		AND    a.Active_Flag = 1
		AND    b.Original_Tweet_Id = ''
		AND    b.In_Reply_To_User_id IS NULL
		ORDER BY TweetTimestamp DESC;

	ELSEIF tweet_type = 'RETWEET' THEN
		SELECT a.Topic_Entity_Id as TopicID , a.Entity_Value as TopicName, b.Text as TweetMsg, b.Tweet_Date as TweetTimestamp, b.User_Screen_Name as TweetHandle, 
			   b.Tweet_Id as TweetID, c.Sentiment_Type as SentimentType, c.Sentiment_Percentage as SentimentPercent 
		FROM   topic_entities_tbl a,   
			   twitter_data_tbl b, 
			   twitter_sentiments_tbl c
		WHERE  a.Topic_Entity_Id = b.Topic_Entity_Id
		AND    b.Tweet_Id = c.Tweet_Id
		AND    a.Active_Flag = 1
		AND    b.Original_Tweet_Id <> ''
		AND    b.In_Reply_To_User_id IS NULL
		ORDER BY TweetTimestamp DESC;

	ELSEIF tweet_type = 'REPLY' THEN
		SELECT a.Topic_Entity_Id as TopicID , a.Entity_Value as TopicName, b.Text as TweetMsg, b.Tweet_Date as TweetTimestamp, b.User_Screen_Name as TweetHandle, 
			   b.Tweet_Id as TweetID, c.Sentiment_Type as SentimentType, c.Sentiment_Percentage as SentimentPercent 
		FROM   topic_entities_tbl a,   
			   twitter_data_tbl b, 
			   twitter_sentiments_tbl c
		WHERE  a.Topic_Entity_Id = b.Topic_Entity_Id
		AND    b.Tweet_Id = c.Tweet_Id
		AND    a.Active_Flag = 1
		AND    b.In_Reply_To_User_id IS NOT NULL
		ORDER BY TweetTimestamp DESC;
        
	END IF;
END$$
DELIMITER ;
										     
									       

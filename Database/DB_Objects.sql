-- Create schema
CREATE SCHEMA `dapproject` ;

-- Create Tables

CREATE TABLE `dapproject`.`topics_tbl` (
  `Topic_Id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NOT NULL,
  `Description` VARCHAR(200) NULL,
  `Active_Flag` INT NOT NULL,
  `Created_Date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` TIMESTAMP,
  PRIMARY KEY (`Topic_Id`),
  UNIQUE KEY `topic_uk01` (`Name`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8;
  

CREATE TABLE `dapproject`.`topic_entities_tbl` (
  `Topic_Entity_Id` INT NOT NULL AUTO_INCREMENT,
  `Topic_Id` INT NOT NULL,
  `Entity_Type` ENUM('HASHTAG', 'TWITTER_HANDLE', 'KEYWORD', 'OTHER') NOT NULL,
  `Entity_Value` VARCHAR(200) NOT NULL,
  `Active_Flag` INT NOT NULL,
  `Created_Date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` TIMESTAMP,
  PRIMARY KEY (`Topic_Entity_Id`),
  UNIQUE KEY `topic_entities_uk01` (`Topic_Id`, `Entity_Type`, `Entity_Value`),
  CONSTRAINT `topic_entities_fk01` FOREIGN KEY (`Topic_Id`) REFERENCES `dapproject`.`topics_tbl` (`Topic_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8;  
  
  
CREATE TABLE `dapproject`.`twitter_data_tbl` (
  `Tweet_Id` VARCHAR(100) NOT NULL,
  `Tweet_Date` TIMESTAMP DEFAULT 0,
  `Text` VARCHAR(250),
  `Hashtag` VARCHAR(250),
  `Expanded_Url` VARCHAR(250),
  `iso_language_code` VARCHAR(250),
  `in_reply_to_status_id` VARCHAR(250),
  `in_reply_to_user_id` VARCHAR(250),
  `in_reply_to_screen_name` VARCHAR(250),
  `User_Id` VARCHAR(250),  
  `User_Name` VARCHAR(250),
  `User_Screen_Name` VARCHAR(250),
  `User_Location` VARCHAR(250),
  `Original_Tweet_Id` VARCHAR(100),
  `Original_Tweet_Date` TIMESTAMP DEFAULT 0,
  `Original_Text` VARCHAR(250),
  -- `Original_Hashtag` VARCHAR(250),
  -- `Original_Expanded_Url` VARCHAR(250),
  -- `Original_iso_language_code` VARCHAR(250),
  `Original_User_Id` VARCHAR(250),  
  `Original_User_Name` VARCHAR(250),
  `Original_User_Screen_Name` VARCHAR(250),
  `Original_User_Location` VARCHAR(250),
  `Topic_Entity_Id` INT NOT NULL,
  `Created_Date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` TIMESTAMP,
  PRIMARY KEY (`Tweet_Id`),
  CONSTRAINT `twitter_data_fk01` FOREIGN KEY (`Topic_Entity_Id`) REFERENCES `dapproject`.`topic_entities_tbl` (`Topic_Entity_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8;  
  
  
CREATE TABLE `dapproject`.`twitter_sentiments_tbl` (
  `Tweet_Sentiment_Id` INT NOT NULL AUTO_INCREMENT,
  `Tweet_Id` VARCHAR(100) NOT NULL,
  `Topic_Entity_Id` INT NOT NULL,
  `Sentiment_Type` ENUM('POSITIVE', 'NEGATIVE', 'NEUTRAL') NOT NULL,
  `Sentiment_Percentage` INT,
  `Created_Date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` TIMESTAMP,
  PRIMARY KEY (`Tweet_Sentiment_Id`),
  CONSTRAINT `twitter_sentiments_fk01` FOREIGN KEY (`Tweet_Id`) REFERENCES `dapproject`.`twitter_data_tbl` (`Tweet_Id`),
  CONSTRAINT `twitter_sentiments_fk02` FOREIGN KEY (`Topic_Entity_Id`) REFERENCES `dapproject`.`topic_entities_tbl` (`Topic_Entity_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8; 
 
 
   CREATE TABLE `dapproject`.`events_log_tbl` (
    `Event_Log_Id` INT NOT NULL AUTO_INCREMENT,
    `Topic_Entity_Id` INT NOT NULL,
    `Start_Time` TIMESTAMP NOT NULL  DEFAULT 0,
    `End_Time` TIMESTAMP NOT NULL  DEFAULT 0,
    `Records_Processed` INT,
    `Status` ENUM('SUCCESS', 'FAIL') NOT NULL,
    `Created_Date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `Modified_Date` TIMESTAMP,
    PRIMARY KEY (`Event_Log_Id`),
    CONSTRAINT `events_log_fk01` FOREIGN KEY (`Topic_Entity_Id`) REFERENCES `dapproject`.`topic_entities_tbl` (`Topic_Entity_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8; 

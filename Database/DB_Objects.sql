-- Create schema
CREATE SCHEMA `ptsm` ;

-- Create Tables

CREATE TABLE `ptsm`.`topics_tbl` (
  `Topic_Id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Description` VARCHAR(500) NULL,
  `Active_Flag` INT NOT NULL,
  `Created_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Topic_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;

CREATE TABLE `ptsm`.`topic_entities_tbl` (
  `Topic_Entity_Id` INT NOT NULL AUTO_INCREMENT,
  `Topic_Id` INT NOT NULL,
  `Entity_Type` ENUM('HASHTAG', 'TWITTER_HANDLE', 'KEYWORD', 'OTHER') NOT NULL,
  `Entity_Value` VARCHAR(500) NOT NULL,
  `Active_Flag` INT NOT NULL,
  `Created_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Topic_Entity_Id`),
  UNIQUE KEY `topic_entities_uk01` (`Topic_Id`, `Entity_Type`, `Entity_Value`),
  CONSTRAINT `topic_entities_fk01` FOREIGN KEY (`Topic_Id`) REFERENCES `ptsm`.`topics_tbl` (`Topic_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;  
  
  
CREATE TABLE `ptsm`.`twitter_data_tbl` (
  `Tweet_Id` VARCHAR(100) NOT NULL,
  `Tweet_Date` DATETIME,
  `Text` VARCHAR(1000),
  `Hashtag` VARCHAR(500),
  `Expanded_Url` VARCHAR(1000),
  `iso_language_code` VARCHAR(500),
  `in_reply_to_status_id` VARCHAR(500),
  `in_reply_to_user_id` VARCHAR(500),
  `in_reply_to_screen_name` VARCHAR(500),
  `User_Id` VARCHAR(500),  
  `User_Name` VARCHAR(500),
  `User_Screen_Name` VARCHAR(500),
  `User_Location` VARCHAR(500),
  `Original_Tweet_Id` INT,
  `Original_Tweet_Date` DATETIME,
  `Original_Text` VARCHAR(1000),
  -- `Original_Hashtag` VARCHAR(500),
  -- `Original_Expanded_Url` VARCHAR(5000),
  -- `Original_iso_language_code` VARCHAR(500),
  `Original_User_Id` VARCHAR(500),  
  `Original_User_Name` VARCHAR(500),
  `Original_User_Screen_Name` VARCHAR(500),
  `Original_User_Location` VARCHAR(500),
  `Topic_Entity_Id` INT NOT NULL,
  `Created_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Tweet_Id`),
  CONSTRAINT `twitter_data_fk01` FOREIGN KEY (`Topic_Entity_Id`) REFERENCES `ptsm`.`topic_entities_tbl` (`Topic_Entity_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4;  
  
  
CREATE TABLE `ptsm`.`twitter_sentiments_tbl` (
  `Tweet_Sentiment_Id` INT NOT NULL AUTO_INCREMENT,
  `Tweet_Id` VARCHAR(100) NOT NULL,
  `Topic_Entity_Id` INT NOT NULL,
  `Sentiment_Type` ENUM('POSITIVE', 'NEGATIVE', 'NEUTRAL') NOT NULL,
  `Sentiment_Percentage` INT NOT NULL,
  `Created_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Modified_Date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Tweet_Sentiment_Id`),
  CONSTRAINT `twitter_sentiments_fk01` FOREIGN KEY (`Tweet_Id`) REFERENCES `ptsm`.`twitter_data_tbl` (`Tweet_Id`),
  CONSTRAINT `twitter_sentiments_fk02` FOREIGN KEY (`Topic_Entity_Id`) REFERENCES `ptsm`.`topic_entities_tbl` (`Topic_Entity_Id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=UTF8MB4; 
  

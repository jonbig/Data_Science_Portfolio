/***********************************************************************/
/*SQL Data Cleaning/Preprocessing Contribution Data Scraped from tracer*/
/***********************************************************************/

/*Creating table in MYSQL Workbench*/

CREATE TABLE `colorado_project`.`contribution_data` (
  `committee_id` VARCHAR(45) NOT NULL,
  `amount` DECIMAL NULL,
  `date` VARCHAR(45) NOT NULL,
  `last_name` VARCHAR(45) NULL,
  `first_name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` DECIMAL NULL,
  `zipcode` VARCHAR(45) NULL,
  `contribution_type` VARCHAR(45) NULL,
  `contributor_type` VARCHAR(45) NULL,
  `electioneering` VARCHAR(45) NULL,
  `committee_type` VARCHAR(45) NULL,
  `committee_name` VARCHAR(45) NULL,
  `candidate_name` VARCHAR(45) NULL,
  `employer` VARCHAR(45) NULL,
  `occupation` VARCHAR(45) NULL,
  `jurisdiction` VARCHAR(45) NULL,

  
/*****************************************/

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\contribution_data.csv" 
INTO TABLE contribution_data CHARACTER 
SET latin1 FIELDS TERMINATED 
BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' ;

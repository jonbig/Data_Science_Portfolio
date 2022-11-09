/********************************************************************/
/*SQL Data Cleaning/Preprocessing Candidate Data Scrape from tracer*/
/********************************************************************/

/*Creating table in MYSQL Workbench*/

CREATE TABLE `colorado_project`.`candidate_data` (
  `candidate_name` VARCHAR(45) NULL,
  `candidate_email` VARCHAR(45) NULL,
  `candidate_id` VARCHAR(45) NULL,
  `committee_id` VARCHAR(45) NULL,
  `committee_address` VARCHAR(45) NULL,
  `website` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `political_party` VARCHAR(45) NULL,
  `office` VARCHAR(45) NULL,
  `district` VARCHAR(45) NULL,
  `committee_name` VARCHAR(45) NULL,
  `mailing_address` VARCHAR(45) NULL,
  `registered_agent` VARCHAR(45) NULL,
  `agent_email` VARCHAR(45) NULL,
  PRIMARY KEY (`committee_id`));
  
/*****************************************/

/*Loading data into SQL table*/

LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\candidate_data_test.csv" 
INTO TABLE candidate_data CHARACTER SET latin1 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' ;

/*****************************************/

/*Changing name column from 'last, first' to 'first last' format */

UPDATE candidates
SET candidate_name = CONCAT( 
  SUBSTRING(candidate_name, LOCATE(',', candidate_name) + 2, LENGTH(candidate_name) - LOCATE(',', candidate_name) - 1),
  ' ',
  SUBSTRING(candidate_name, 1, LOCATE(',', candidate_name) - 1)
)
WHERE candidate_name = 'AHREND, JARED';

/*****************************************/

/*Changing text in political party column */

UPDATE candidate_data
SET political_party = 'Democrat'
WHERE political_party = 'Democratic'

/*****************************************/



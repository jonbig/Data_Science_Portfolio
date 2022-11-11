/*****************************************************************************************/
/*SQL code data cleaning, processing, and table joins for Voting District Locator Project*/
/*****************************************************************************************/

/*Cleaning & Processing Candidate Data Scraped from Colorado Secretary of State*/

/*Candidate Data*/
/*Creating table in MYSQL Workbench*/
CREATE TABLE `colorado_project`.`candidate_data` (
  `candidate_name` VARCHAR(45) NULL,
  `candidate_email` VARCHAR(45) NULL,
  `candidate_id` VARCHAR(45) NULL,
  `committee_id` VARCHAR(45) NOT NULL,
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

/*Loading data into candidate SQL table*/
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\candidate_data.csv" 
INTO TABLE candidate_data CHARACTER SET latin1 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' ;

/*****************************************/

/*Changing name column from 'last, first' to 'first last' format*/
UPDATE candidate_data
SET candidate_name = CONCAT( 
  SUBSTRING(candidate_name, LOCATE(',', candidate_name) + 2, LENGTH(candidate_name) - LOCATE(',', candidate_name) - 1),
  ' ',
  SUBSTRING(candidate_name, 1, LOCATE(',', candidate_name) - 1)
)

/*****************************************/

/*Changing text in political party column */
UPDATE candidate_data
SET political_party = 'Democrat'
WHERE political_party = 'Democratic'

/*****************************************/

/*Removing any trailing spaces*/
UPDATE candidate_data
SET candidate_name = RTRIM(candidate_name)

/*****************************************/

/*Cleaning candidate names*/
UPDATE candidate_data
SET candidate = 'TONY EXUM'
WHERE candidate = 'THOMAS EXUM'

UPDATE candidate_data
SET candidate = 'STEPHEN VARELA'
WHERE candidate = 'STEPHEN VARELA,'

UPDATE candidate_data
SET candidate = 'SAID SHARBINI,'
WHERE candidate = 'SAID SHARBINI'

UPDATE candidate_data
SET candidate = 'ROSE PUGLIESE'
WHERE candidate = 'ROSE PUGLIESE,'

UPDATE candidate_data
SET candidate = 'NATHAN BAXTER'
WHERE candidate = 'NATHAN BAXTER,'

UPDATE candidate_data
SET candidate = 'MATT SOLOMON'
WHERE candidate = 'MATT SOLOMON,'

/*****************************************/


/*Contributions Data*/
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
  
/*Reformatting dates*/  
UPDATE contributions_data
SET date = STR_TO_DATE(date, '%c/%e/%Y %r');
 
/*****************************************/
  
/*Editing categories*/  
UPDATE contributions
SET contributor_type = 'Corporation'
WHERE contributor_type = 'LLC'
  
UPDATE contributions
SET contributor_type = 'Corporation'
WHERE contributor_type = 'Business'

/*****************************************/

/*Loading data into table*/
LOAD DATA INFILE "C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\contribution_data.csv" 
INTO TABLE contribution_data CHARACTER 
SET latin1 FIELDS TERMINATED 
BY ',' ENCLOSED BY '"' 
LINES TERMINATED BY '\r\n' ;

/*****************************************/  
  
/*Removing extra numbers from data column*/
UPDATE contribution_data
SET date = LEFT(date, LENGTH(date)-5)
  
/*****************************************/
  
/*Table Joins for Data Visualizations*/

/*Total Contributions by Candidate Viz*/

SELECT candidate_data.candidate_name, candidate_data.district, sum(contribution_data.amount) AS total_contributions
FROM candidate_data
LEFT JOIN contribution_data
ON candidate_data.committee_id = contribution_data.recipient_committee_id
GROUP BY candidate_data.candidate_name;

  

  



  
  
  
  
  
  


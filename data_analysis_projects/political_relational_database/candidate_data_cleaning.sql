/********************************************************************/
/* SQL Data Cleaning/Preprocessing Candidate Data Scrape from tracer*/
/********************************************************************/

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

/*Select all the tables*/

/*****************************************/

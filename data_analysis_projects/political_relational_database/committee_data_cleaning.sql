/********************************************************************/
/*SQL Data Cleaning/Preprocessing Committee Data Scraped from tracer*/
/********************************************************************/

/*Creating table in MYSQL Workbench*/

CREATE TABLE `colorado_project`.`committee_data` (
  `committee_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `committee_id` VARCHAR(45) NOT NULL,
  `committee_type` VARCHAR(45) NULL,
  `committee_purpose` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `agent` VARCHAR(45) NULL,
  `expenditures` DECIMAL NULL,
  `contributions` DECIMAL NULL,
  `ending_balance` DECIMAL NULL,
  PRIMARY KEY (`committee_id`));
  
/*****************************************/

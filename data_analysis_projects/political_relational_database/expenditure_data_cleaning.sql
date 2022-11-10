CREATE TABLE `colorado_project`.`expenditure_data` (
  `committee_id` VARCHAR(45) NOT NULL,
  `amount` DECIMAL NULL,
  `date` VARCHAR(45) NULL,
  `recipient_name` VARCHAR(45) NULL,
  `address` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `zipcode` VARCHAR(45) NULL,
  `expenditure_type` VARCHAR(45) NULL,
  `electioneering` VARCHAR(45) NULL,
  `committee_type` VARCHAR(45) NULL,
  `committee_name` VARCHAR(45) NULL,
  `candidate_name` VARCHAR(45) NULL,
  `jurisdiction` VARCHAR(45) NULL)
  
  
  
  
UPDATE expenditure_data
SET date = LEFT(date, LENGTH(date)-5)

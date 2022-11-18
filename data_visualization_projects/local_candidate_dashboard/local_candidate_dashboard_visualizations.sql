/*****************************************************************************************/
/*SQL code for voter district visualizations*/
/*****************************************************************************************/
  
/*Candidate Info Text Table Viz*/

SELECT candidate_name, district, candidate_email, political_party, website
FROM .candidate_data;

/*****************************************/


/*Total Contributions by Candidate Viz*/

SELECT candidate_data.candidate_name, candidate_data.district, sum(contribution_data.amount) AS total_contributions
FROM candidate_data
LEFT JOIN contribution_data
ON candidate_data.committee_id = contribution_data.recipient_committee_id
GROUP BY candidate_data.candidate_name;
  
/*****************************************/
  
  
/*Fundraising Profile Pie Chart*/  
  
SELECT alias.recipient_name, SUM(alias.contribution_amount), alias.contributor_type, candidate_data.district
FROM contribution_data AS alias
LEFT JOIN candidate_data 
ON alias.recipient_committee_id = candidate_data.committee_id
GROUP BY alias.recipient_name, alias.contributor_type
HAVING district IS NOT NULL
ORDER BY alias.recipient_name
  
  
/*****************************************/

/*Super PAC Activity*/  

SELECT alias.recipient_name, SUM(alias.contribution_amount), alias.expenditure_type, alias.committee_name, alias.candidate_name, candidates.district, committee_data.committee_purpose
FROM expenditure_data AS alias
LEFT JOIN candidates 
ON alias.recipient_name = candidate_data.candidate_name
LEFT JOIN committee_data
ON alias.committee_name = committee_data.committee_name
GROUP BY committee_name
HAVING expenditure_type = 'Independent Expenditures'

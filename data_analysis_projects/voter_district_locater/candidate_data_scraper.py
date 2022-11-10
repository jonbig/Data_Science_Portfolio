#This scraper extracts candidate data from the Colorado Secretary of State website that would otherwise have to be manually collected.

#imports
from cgitb import text
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd
from selenium.webdriver.chrome.options import Options

#to reduce error messages
options = Options()
browser_options = Options()
browser_options.headless = True

options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')


#setup chromedriver
path = ("C:/Users/Jonbi/Desktop/coding_projects/chromedriver.exe")
s = Service(path)
driver = webdriver.Chrome(service=s)



driver.get("https://tracer.sos.colorado.gov/PublicSite/homepage.aspx") #goes to tracer homepage

search = driver.find_element(By.ID,"_ctl0_LeftMenu_hlnkSearch") #clicks "search" and waits 5 seconds"
search.click()
time.sleep(2)

candidate_search = driver.find_element(By.ID,"_ctl0_LeftMenu_hlnkSearchCandidates") #clicks candidate search and waits 5 seconds
candidate_search.click()
time.sleep(2)

select_election_year = Select(driver.find_element(By.ID,'_ctl0_Content_lstElectionYear')) #selects election year
select_election_year.select_by_index(5)
time.sleep(2)

select_jurisdiction = Select(driver.find_element(By.ID,"_ctl0_Content_ddlJurisdiction")) #selects "statewide" jurisdiction
select_jurisdiction.select_by_index(2)
time.sleep(2)

#change this for different races
select_office = Select(driver.find_element(By.ID,"_ctl0_Content_ddlOffice")) #selects "colorado senate" office
select_office.select_by_index(15)
time.sleep(2)

search_button = (driver.find_element(By.ID,"_ctl0_Content_btnSearch")) #clicks the search button
search_button.click()
time.sleep(2)

#page_size = Select(driver.find_element(By.ID,"_ctl0_Content_dgdSearchResults__ctl13_dgdSearchResultsPageSizeDropDown")) #sets page size to 50
#page_size.select_by_index(2)
#time.sleep(5)

#change for different page numbers
#page_select = (driver.find_element(By.ID,"_ctl0_Content_dgdSearchResults__ctl53_dgdSearchResultsPageLink3")) #clicks a page of search results (change last number only)
#page_select.click()
#time.sleep(5)



link_elements_list = driver.find_elements(By.XPATH, "//a[@class='grdBodyDisplay']") #creats a list of HTML elements associated with each othe 50 dispayed committee links
committee_ids_list = [] #empty list to store href values extraced from full html element
for link in link_elements_list: #iterates through the list of html elements and extracts each id value and adds it to a new list
    committee_link = link.get_attribute('id')
    committee_ids_list.append(committee_link)
time.sleep(5)


for id in committee_ids_list: #iterates thorugh a list of ids to click each committe link
    select_id = driver.find_element(By.ID,(id))  # navigates to the committee link page and clicks
    select_id.click()
    time.sleep(5)
    
    try:
        candidate_name = (driver.find_element(By.ID,"_ctl0_Content_lblCandName")).text  # finds candidate's first and last name  
    except:
        candidate_name = "None"

    try:
        candidate_email = driver.find_element(By.ID, '_ctl0_Content_lnkCandEmail').text #finds candidate email address
    except:
        candidate_email = 'None'
       
    try:
        candidate_committee_id = driver.find_element(By.ID, '_ctl0_Content_lblCommitteeID').text #finds candidate committee id #
    except:
        candidate_committee_id = 'None' 

    try:
        candidate_id = driver.find_element(By.ID, '_ctl0_Content_lblCandidateID').text #finds candidate id #
    except:
        candidate_id = 'None' 
    
    try:
        candidate_url = driver.find_element(By.ID, '_ctl0_Content_lnkCandWeb').text #finds candidate url
    except:
        candidate_url = 'None'
    try:
        candidate_mailing_address = (driver.find_element(By.ID,"_ctl0_Content_lblCandMailAddress1")).text  # finds candidate's mailing address
        
    except:
        candidate_mailing_address = "None"

    try:
        candidate_website = (driver.find_element(By.ID,"_ctl0_Content_lnkCandWeb")).text  # finds candidate's website
        
    except:
        candidate_website = "None"

    try:
        candidate_phone = (driver.find_element(By.ID,"_ctl0_Content_lblCandPhone")).text  # finds candidate's phone number
       
    except:
        candidate_phone = "None"

    try:
        candidate_email = (driver.find_element(By.ID,"_ctl0_Content_lnkCandEmail")).text  # finds candidate's email
        
    except:
        candidate_email = "None"

    try:
        candidate_party = (driver.find_element(By.ID,"_ctl0_Content_lblCandParty")).text  # finds candidate's party
        

    except:
        candidate_party = "None"

    try:
        candidate_office = (driver.find_element(By.ID,"_ctl0_Content_lblCandOffice")).text  # finds candidate's office
        
    except:
        candidate_office = "None"

    try:
        candidate_district = (driver.find_element(By.ID,"_ctl0_Content_lblCandDistrict")).text  # finds candidate's district
        
    except:
        candidate_district = "None"

    try:
        candidate_committee_name = (driver.find_element(By.ID,"_ctl0_Content_lblCommName")).text  # finds candidate's committee name
       
    except:
        candidate_committee_name = "None"

    try:
        candidate_committee_mailing = (driver.find_element(By.ID,"_ctl0_Content_lblCommMailAddress1")).text  # finds candidate's committee mailing address
        
    except:
        candidate_committee_mailing = "None"

    try:
        candidate_registered_agent = (driver.find_element(By.ID,"_ctl0_Content_lblRegisteredAgent")).text  # finds candidate's registered agent
        
    except:
        candidate_registered_agent = "None"

    try:
        registered_agent_email = (driver.find_element(By.ID,"_ctl0_Content_lnkAgentEmail")).text  # finds candidate's registered agent's email
        
    except:
        registered_agent_email = "None"

    try:
        expenditures = (driver.find_element(By.ID,"_ctl0_Content_lblCandidateExpenditures_EC")).text  # finds total expenditures
        
    except:
        expenditures = "None"

    try:
        contributions = (driver.find_element(By.ID,"_ctl0_Content_lblTotalCont_EC")).text  # finds contributions
        
    except:
        contributions = "None"

    try:
        ending_balance = (driver.find_element(By.ID,"_ctl0_Content_lblEndingBalance_EC")).text  # finds ending balance
        
    except:
        ending_balance = "None"

       
       
    dic = {'candidate_name': {candidate_name}, 'candidate_email': {candidate_email}, 'candidate_committee_id' :{candidate_committee_id}, 'candidate_id': {candidate_id}, 'candidate_url': {candidate_url}, 'candidate_mailing_address': {candidate_mailing_address}, 'candidate_website':{candidate_website},
    'candidate_phone': {candidate_phone},'candidate_party': {candidate_party}, 'candidate_office': {candidate_office}, candidate_district: {candidate_district}, 'candidate_committee_name': {candidate_committee_name},
   'candidate_committee_mailing': {candidate_committee_mailing}, 'candidate_registered_agent': {candidate_registered_agent}, 'registered_agent_email': {registered_agent_email}, 'expenditures': {expenditures}, 
   'contributions': {contributions}, 'ending_balance': {ending_balance}}
    
    

    df = pd.DataFrame([dic])
    df.to_csv('candidate_data_test.csv', mode='a', header=False)

    driver.back()
    driver.refresh()

    ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

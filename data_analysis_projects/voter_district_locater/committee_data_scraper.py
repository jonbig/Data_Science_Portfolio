#This scraper extracts committee data from the Colorado Secretary of State website that would otherwise have to be manually collected. 

#import relevent stuff
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
time.sleep(5)

committee_search = driver.find_element(By.XPATH,'/html/body/form/div[1]/table[2]/tbody/tr[3]/td[1]/table/tbody/tr/td[2]/table/tbody/tr/td/div/ul/li[2]/ul/li[2]/a') #clicks committee search and waits 5 seconds
committee_search.click()
time.sleep(2)


select_committee_type = Select(driver.find_element(By.ID,'_ctl0_Content_ddlCommitteeType')) #selects committee type
select_committee_type.select_by_index(4)
time.sleep(2)


#select_jurisdiction = Select(driver.find_element(By.ID,"_ctl0_Content_ddlJurisdiction")) #selects "statewide" jurisdiction
#select_jurisdiction.select_by_index(2)
#time.sleep(10)


search_button = (driver.find_element(By.ID,"_ctl0_Content_btnSearch")) #clicks the search button
search_button.click()
time.sleep(5)

page_size = Select(driver.find_element(By.ID,"_ctl0_Content_dgdSearchResults__ctl13_dgdSearchResultsPageSizeDropDown")) #sets page size to 50
page_size.select_by_index(2)
time.sleep(2)

#change for different page numbers
page_select = (driver.find_element(By.ID,"_ctl0_Content_dgdSearchResults__ctl53_dgdSearchResultsPageLink2")) #clicks a page of search results (change last number only)
page_select.click()
time.sleep(5)



link_elements_list = driver.find_elements(By.XPATH, "//a[@class='grdBodyDisplay']") #creats a list of HTML elements associated with each othe 50 dispayed committee links
committee_ids_list = [] #empty list to store href values extraced from full html element
for link in link_elements_list: #iterates through the list of html elements and extracts each id value and adds it to a new list
    committee_link = link.get_attribute('id')
    committee_ids_list.append(committee_link)
time.sleep(5)


for id in committee_ids_list: #iterates thorugh a list of ids to click each committee link
    select_id = driver.find_element(By.ID,(id))  # navigates to the committee link page and clicks
    select_id.click()
    time.sleep(5)
    
    try:
        committee_name = (driver.find_element(By.ID,"_ctl0_Content_lblCommName")).text  # finds comm name 
    except:
        committee_name = "None"

    try:
        agent_email = driver.find_element(By.ID, '_ctl0_Content_lnkAgentEmail').text #finds comm email address
    except:
        agent_email = 'None'
       
    try:
        committee_id = driver.find_element(By.ID, '_ctl0_Content_lblCommitteeID').text #finds comm committee id #
    except:
        committee_id = 'None' 
       
    try:
        committee_type = driver.find_element(By.ID, '_ctl0_Content_lblCommType').text #finds comm type
    except:
        committee_type = 'None' 

    try:
        committee_purpose = driver.find_element(By.ID, '_ctl0_Content_lblCommPurpose').text  #finds comm purpose
    except:
        candidate_purpose = 'None'

    try:
        committee_phone = (driver.find_element(By.ID,"_ctl0_Content_lblCommPhone")).text  # finds comm's phone number
       
    except:
        committee_phone = "None"


    try:
        candidate_registered_agent = (driver.find_element(By.ID,"_ctl0_Content_lblRegisteredAgent")).text  # finds comm registered agent
        
    except:
        candidate_registered_agent = "None"


    try:
        expenditures = (driver.find_element(By.ID,"_ctl0_Content_lblTotalExp_EC")).text  # finds total expenditures
        
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


    dic = {'committee_name': {committee_name}, 'agent_email': {agent_email}, 'committee_id' :{committee_id}, 'committee_type': {committee_type}, 'committee_purpose': {committee_purpose}, 
    'committee_phone': {committee_phone}, 'candidate_registered_agent': {candidate_registered_agent},'expenditures': {expenditures}, 'contributions': {contributions}, 'ending_balance': {ending_balance}}
    

    df = pd.DataFrame([dic])
    df.to_csv('committee_data_test.csv', mode='a', header=False)

    driver.back()
    driver.refresh()

    ActionChains(driver).key_down(Keys.RETURN).key_up(Keys.RETURN).perform()

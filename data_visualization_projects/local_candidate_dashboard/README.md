# Local Candidate Dashboard

_The visualizations made in this project are part of a much larger project designed to allow Colorado voters to easily research the political candidates and committees active in their local area. [Click here to view and interact with the full project.](https://public.tableau.com/app/profile/jon.biggerstaff/viz/ColoradoPoliticalSpendingTrackerUpdated/DistrictDash?publish=yes)_


## **1. Ask questions and define the problem.**

Media and news outlets often neglect to cover state and local elections. As a result, most voters don’t know which candidates they are choosing between until they are completing their ballot. In this project we will build an interactive dashboard that will allow voters in Colorado to quickly and easily find their state legislative districts along with the candidates running for office in the district. The dashboard will also display candidate fundraising information and information on any super PACs that are actively spending money in the district.

The dashboard is made up of 6 visualizations:

- District Locator- Allows voters to quickly identify their state house and senate districts and filters the remaining visualizations to display data relevant to the selected district.

- Candidate Info Table- Displays a table of information associated with the candidates in the selected legislative district. 

- Total Donations- A simple bar chart comparing the fundraising totals of candidates in the selected legislative district. 

- Fundraising profile- Pie charts drilling down into each candidate’s fundraising total by contribution type, giving voters an idea of the candidate’s overall fundraising strategy. The wedges in these pie charts act as filters for the Donor Details visualization

- Super PAC Activity- Super PACs make up the majority of political spending in many competitive elections. If we’re not examining their spending, we’re missing most of the picture. This stacked bubble chart acts as a filter for the Political Committee Research Dashboard. For example, a voter notices that Super PAC XYZ has spent $100,000 supporting candidate John Smith. Clicking on the bubble associated with Super PAC XYZ will automatically filter the Political Committee Research Dashboard to display information associated with Super PAC XYZ.

- Donor Details- A table that displays the contributor name, and contribution amount. This table is filtered by clicking a wedge in the fundraising profile pie chart. For example, a voter sees that candidate John Smith has received 33% of their money from PACs, clicking on that wedge will filter this table to display the names of those pacs and their respective contribution amounts to John Smith. Voters can also click on any of these committees to filter the Political Committee Research Dashboard to display information associated with the selected committee.

This project includes:

- Python with Pandas and Selenium: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)
- ArcMap (for manipulating shapefiles)

## **2. Prepare data by collecting and storing the information.**

**Candidate and Committee Data**

All data on state legislative candidates can be found at the Colorado Secretary of State’s website. Unfortunately, there are no available reports that include important attributes like the candidate’s district, political party etc. Copying and pasting this data for hundreds of candidates would be incredibly time consuming, so I built a simple web scraper in python to automate the process. The scraper saves all of the data as a CSV file. 

[The python code for the candidate data scraper has been uploaded to this project folder.](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/local_candidate_dashboard/candidate_committee_scraper.py)

[The python code for the committee data scraper has been uploaded to this project folder.](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/local_candidate_dashboard/committee_scraper.py)

**District Geographical Data**

The shapefiles containing polygon data for each legislative district are easily downloaded from public sources. There are separate shapefiles for the Colorado House and Colorado Senate, so I used ArcMap to combine them into a single table.

**Contribution and Expenditure Data**

The contribution and expenditure data can be downloaded in bulk in csv form. 

## **3. Process data by cleaning and checking the information.**

The next step is to upload the 4 data datasets into MySQL Workbench to clean and process the data with SQL. [Click here to view the SQL code used to clean the data for all 4 tables](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/local_candidate_dashboard/local_candidate_dashboard_data_cleaning.sql)

## **4. Analyze data to find patterns, relationships, and trends.**

Now that the data is cleaned, the next step is to build the tables needed for each of the 3 visualizations. This isn't strictly necessary as Tableau supports table merges natively. However, I've found that using SQL joins and connecting Tableau to the resulting tables yeilds more responsive visualizations. 

[The SQL code for all of these visualizations can be found here.](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/local_candidate_dashboard/local_candidate_dashboard_visualizations.sql)

**District Locator**

Since this is a shapefile, we will connect it to Tableau directly. We will define a one to many relationship with the other tables based on the district field. This is similar to a SQL join on the district field, but using tableau's relationship function allows us to keep the shapefile intact. Lastly, we will add a filter that allows the voter to select betwen displaying the Colorado House Districts and the Colorado Senate Districts. The district locator will act as a filter for the remaining visualizations in this dashboard. For example, a voter uses the map to determine they live in Colorado House District 8, they simply click the district and the dashboard is automatically filtered to only display information (candidates etc) associated with House District 8. This means that each table will need to contain a districts field.

![dist_loc](https://user-images.githubusercontent.com/102785707/202817780-b1da1625-dedc-41c3-baaa-c9def7a18123.PNG)


**Candidate Info Table**

This text table is built from the candidates table with a simple select query in SQL.

![test2](https://user-images.githubusercontent.com/102785707/202818093-bbe7016b-5e3d-4a84-b194-450de74b581f.PNG)


**Total Donations**

This horizontal bar chart will display the candidate's name along with the total dollar amount of contributions they've received. I'll use SQL to join the data from the contributions table with the candidates table on the committee ID field. We can then group the resulting table by candidate name and the sum of the contribution amounts. 

![test1](https://user-images.githubusercontent.com/102785707/202817963-1e3ce415-5566-4c1c-b87f-8a2e93d09740.PNG)


**Fundraising Profile**

This pie chart will show the proportional contribution types for each candidate's fundraising. To create the chart we will use aggregate functions in SQL to group the contributions by candidate and contributor type and join the resulting table with the candidates table in order to populate the respective legislative districts.

**Super PAC Activity**

This stacked bubble chart will tell voters which super PACs are making political expenditures in their local district. We will need to first join the expenditures data with the candidates table so that each expenditure is associated with a legislative district. We’ll also need to join the expenditures table with the committees table to bring over the purpose of the committee. We’ll then group the table by the committee name, and use the HAVING filter to include only independent expenditures. The last step is to filter the table by district, and that is done automatically when the voter selects their district in the district locator visualization. 

**Donor Details**

This text table allows voters to drill down into the data behind the Fundraising Profile visualization so that they can see the names of the donors that make up whichever wedge was selected.  We can therefore use almost  the same query here as we used for the Fundraising Profile visualization, with the one additional step of including the committee name field from the contributions table.



## **5. Share data with your audience.**

![Capture](https://user-images.githubusercontent.com/102785707/201451088-6da1ab7c-efba-491b-a053-028c362e02ac.PNG)


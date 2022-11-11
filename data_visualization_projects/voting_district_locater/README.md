# Voting District Locator


## **1. Ask questions and define the problem.**

Media and news outlets often neglect to cover state and local elections. As a result, most voters don’t know which candidates they are choosing between until they are completing their ballot. In this project we will design an interactive tool (in the form of a Tableau dashboard) that will allow voters in Colorado to quickly and easily find their state legislative districts, the candidates in those districts, and their relevant contact information. The dashboard will also display fundraising data for each candidate, including the total amount of contributions recieved and what kind of contributions they have received. After election day, we can remove the all but the winning candidates.  This will allow voters to easily see the legislators who represent them, allowing them to reach out via phone or email and build a relationship with their elected officials.

This project includes:

- Python with Pandas and Selenium: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)
- ArcMap (for manipulating shapefiles)

## **2. Prepare data by collecting and storing the information.**

**Candidate Data**

All data on state legislative candidates can be found at the Colorado Secretary of State’s website. Unfortunately, there are no available reports that include important attributes like the candidate’s district, political party etc. Copying and pasting this data for hundreds of candidates would be incredibly time consuming, so I built a simple web scraper in python to automate the process. The scraper saves all of the data as a CSV file. [The python code for this scraper has been uploaded to this project folder.](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/voting_district_locater/candidate_data_scraper.py)

**District Geographical Data**

The shapefiles containing polygon data for each legislative district are easily downloaded from public sources. There are separate shapefiles for the Colorado House and Colorado Senate, so I used ArcMap to combine them into a single table.

**Contribution Data**

The contribution data can be downloaded in bulk in csv form. 

## **3. Process data by cleaning and checking the information.**

The next step is to upload the 3 data datasets into MySQL Workbench to clean and process the data with SQL. [You can view the SQL code here.](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_visualization_projects/voting_district_locater/candidate_data_cleaning.sql)

## **4. Analyze data to find patterns, relationships, and trends.**

Now that the data is cleaned, the next step is to build the tables needed for each of the 3 visualizations. This isn't strictly necessary as Tableau supports table merges natively. However, I've found that using SQL joins and connecting Tableau to the resulting tables yeilds more responsive visualizations. I'll need to create 3 tables for the 3 visualizations in this project. 

Contributions Visualization

This horizontal bar chart will display the candidate's name along with the total dollar amount of contributions they've received. I'll use SQL to join the data from the contributions table with the candidates table on the committee ID field. We can then group the resulting table by candidate name and the sum of the contribution amounts. 

Fundraising Profile Visualization

This pie chart will show the proportional contribution types for each candidate's total fundraising amounts. This will give the voters an idea of how a candidate is funding their campaign. To create the chart we will need

You can view the SQL code for the joins here.





## **5. Share data with your audience.**

The last step is to connect Tableau to our data. There’s a few ways to accomplish this. I have a live connection set up between Tableau and MySQL Workbench, so my only step is to connect Tableau to the shapefile I created earlier. If I was not working with a shapefile I would use SQL to join the tables together and connect tableau to the resulting table. I want to leave the shapefile in .shp format because Tableau will automatically recognize the format and allow me to take advantage of its powerful geographic visualizations. Once the shapefile is connected to Tableau and the live connection with MySQL is established, we can build the dashboard. A screenshot of the resulting dashboard is below. You can view and interact with the dashboard on my Tableau Public page here.


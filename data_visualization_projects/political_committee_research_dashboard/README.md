# Political Committee Research Dashboard

_The visualizations made in this project are part of a much larger project designed to allow Colorado voters to easily research the political candidates and committees active in their local area. [Click here to view and interact with the full project.](https://public.tableau.com/app/profile/jon.biggerstaff/viz/ColoradoPoliticalSpendingTrackerUpdated/DistrictDash?publish=yes)_


## **1. Ask questions and define the problem.**

Every few years the US sets a new record for the most expensive election in our history. Billions of dollars flow into local, state, and national elections from countless different political organizations. Who are these organizations? Where does their money come from? What do they hope to accomplish? In this project we will build a dashboard that empowers Colorado voters with the answers to all of these questions, and many more. 

You will notice that the SQL queries below are missing the WHERE clause. This is because this dashboard is filtered by the voter. For example, the voter uses the Local Candidate Dashboard to find that a super PAC ‘ABC Committee’ has spent $500,000 in their local district, they may then click on ABC Committee which simultaneously brings them to this committee investigator dashboard and filters it to display only information pertaining to ABC Committee. This has the same effect as adding WHERE committee_name = ‘ABC Committee’ to all of the queries below.


The dashboard is made up of 6 visualizations:

- Committee Info- Displays the committee’s name, type, and mission statement in a simple text table.

- Total Committee Fundraising- Displays the total amount of money the committee has received during the present election cycle.

- Fundraising Profile- A pie chart that breaks the total contributions up by contributor type. This allows voters to quickly get an idea of how the committee is being funded.

- Donor Details- Upon clicking a wedge in the fundraising profile pie chart, this text table drills down into the selected data and displays the names of the donors and their donation amounts.

- Total Committee Spending- Displays the total amount of money the committee has spent during the current election cycle along with a pie chart that divides the spending up by expenditure type.

- Electoral Expenditures- This text table shows all of the candidates and campaigns the committee has supported or opposed, along with their district and political affiliation

- Expenditure Detail- This bar chart is filtered by clicking a wedge in the Total Committee Spending pie chart. It displays the names of the top ten recipients of the selected category.

This project includes:

- Python with Pandas and Selenium: (for data gathering)
- SQL (for data processing and table joins)
- Tableau (for data visualization and interactivity)

## **2. Prepare data by collecting and storing the information.**

**Candidate and Committee Data**

All data on state legislative candidates can be found at the Colorado Secretary of State’s website. Unfortunately, there are no available reports that include important attributes like the candidate’s district, political party etc. Copying and pasting this data for hundreds of candidates would be incredibly time consuming, so I built a simple web scraper in python to automate the process. The scraper saves all of the data as a CSV file.

The python code for the candidate data scraper has been uploaded to this project folder here.

The python code for the committee data scraper has been uploaded to this project folder here.

**Contribution and Expenditure Data**

The contribution and expenditure data can be downloaded in bulk in csv form.

## **3. Process data by cleaning and checking the information.**

The next step is to upload the data datasets into MySQL Workbench to clean and process the data with SQL. Many SQL queries were required to clean and process this data. You can view all of those queries here.

## **4. Analyze data to find patterns, relationships, and trends.**

Now that the data is cleaned, the next step is to build the tables needed for each of the visualizations. This isn't strictly necessary as Tableau supports table merges natively. However, I've found that using SQL joins and connecting Tableau to the resulting tables yields more responsive visualizations. The SQL file for all of these visualizations can be found here.

**Committee Info**

The committee data table contains all of the information we need for this text table: committee name, mission statement (or purpose), and committee type. To ensure the dashboards loads as quickly as possible, we can reduce the size of this table by including only the relevant columns:

![comm_1](https://user-images.githubusercontent.com/102785707/205723190-6b25fb72-64b0-4988-92a8-f89a67992633.PNG)

**Total Committee Fundraising**

This text field displays the total amount of money the committee has received. The contribution data table contains all the necessary information, so again we just need to drop the columns we don't need and use a simple sum function:

![comm2](https://user-images.githubusercontent.com/102785707/205723306-24f5ae51-b1c4-4109-ab4f-24d8d65590fc.PNG)

**Fundraising Profile**

This pie chart breaks the total fundraising amount into categories based on the contributor type. This will give the voter a rough idea of how the committee is being funded. We can modify an earlier query slightly to build a table that includes the committee name and total contribution amount by category using an additional group by statement:

![comm3](https://user-images.githubusercontent.com/102785707/205723405-0c383175-7ced-46a6-8c37-2c84a1a90e61.PNG)


**Donor Details**

This text table allows voters to drill down into the data behind the Fundraising Profile visualization so that they can see the names of the donors that make up whichever wedge they have selected. To build the table we will need to group the contribution data table by the committee name and contributor.

![comm4](https://user-images.githubusercontent.com/102785707/205723517-0b4781b3-dc6a-4c68-a085-d8722c897eda.PNG)


**Total Committee Spending**

This text field displays the total amount of money the committee has received. The expenditure data table contains all the necessary information, so we just need to drop the columns, sum the expenditures, and group the results by the committee name.

![comm 5](https://user-images.githubusercontent.com/102785707/205723670-1b458189-6b52-4c93-81b7-56cc54b50fa1.PNG)

**Electoral Expenditures**

This text table displays all of the candidates and campaigns the committee is supporting during this election cycle. It also displays the candidate’s office, district, and political party. This will allow voters to see a snapshot of the committee’s electoral activity. We’ll first need to join the expenditure table with the candidates table so that we have the candidate’s office, district, and political party information. We’ll then group the table by committee name, sum the contribution amounts, and use HAVING to only include the expenditures that are listed as political contributions:

![comm5](https://user-images.githubusercontent.com/102785707/205723787-d4e98179-410e-49c6-8a0d-343e6f544b2a.PNG


**Expenditure Detail**

This text table allows voters to drill down into the data behind the Total Committee Spending visualization so that they can see the names of the recipients that make up whichever wedge they have selected. To build the table we will need to group the expenditure data table by the committee name and 




















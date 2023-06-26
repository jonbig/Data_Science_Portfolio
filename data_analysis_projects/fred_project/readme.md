# [Home Vaues vs Interest Rates](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/voter_turnout_model/final_2019_denver_model.ipynb)

### **Project Overview**

The FRED API (Federal Reserve Economic Data API) provides access to a wide range of economic data from reliable sources such as government agencies and central banks. In this project we will use the FRED API to extract home sales and interest rate data. We will use python to process and combine the data in order to determine how rising interest rates have affected home prices in various geographic regions in the US. 

### Skills

- Python, Plotly, Numpy, Maptplotlib
- Pands, FRED API


### Method

The first step is to search the FRED database for the data I'm interested in. The search returns a dataframe which describes 4 different dataframes of quarterly median home price data, each one corresponding to a different geographic area. 

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/fred_project/fred1.PNG)

We can then loop through the 4 different IDs in the dataframe to extract the data and combine them all into a single dataframe which we can use to build a visualization.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/fred_project/fred3.PNG)

Right away we can see that the Northeast and Western US have the highest home prices in the last 5 years. However, there have been significant increases in home prices for each region since 2018.Next we will use the FRED API to extract data for the average 30 year fixed mortgage rate going back 5 years. Just as we did before, we can use this data to build a visualization.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/fred_project/fred4.png)

After bottoming out in 2021, we can see a sharp increase in mortgage interest rates, topping out near 7% in late 2022. What impact has rising intertest rates had on home prices? Does that impact differ by region? To answer these question, we can use python to combine both of these datasets. Using pyplot we can plot the home prices for each region with the mortgage rate data.

![dist_loc](https://github.com/jonbig/Data_Science_Portfolio/blob/main/data_analysis_projects/fred_project/fred5.png)



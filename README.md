# Forecasting-Ice-Cream-Sales
Using MySQL and Python, I split the data into train and test sets with a test size of 20% and am currently using this data to build a model that predicts sales revenue with 97.55% accuracy when the end-user inputs a temperature.

OBECTIVE:
 This project finds the relationship between the independent variable (outside air temperatures) and its effect on the dependent variable (daily revenue). The goal of this project is to build a model that predicts the daily revenue ($) depending on the temperature (Celsius) outside.


<h2> Data cleaning and importing Python Libraries</h2>
The initial data received in a CSV file  included the columns "Temperature" in Celsius and "Revenue". I wanted to converted temperature from metric to imperial units. So I created a Fahrenheit row in Excel (pictured below). Saved that file and proceeded to my Jupyter Notebook to being the process of analyzing the data with Python.

Next, I imported all Python libraries necessary to analysis the data.

![celsusi](https://user-images.githubusercontent.com/46979334/124637051-deb2b080-de4e-11eb-86e4-f34a8db4309a.PNG)
![MATPLOLIB](https://user-images.githubusercontent.com/46979334/124637217-14579980-de4f-11eb-9582-44a8f67606af.PNG)

<h2> IMPORT RAW DATA</h2>
<li>Imported the raw data csv file using the pandas library
and assigned it to the data frame called “ice cream.</li>
<li>Made backup copies of the original file in case of an error in the integrity of the data.</li>

<p>Here we see the raw data that still includes the “Celsius” column instead of only have two columns “Revenue” and “Temperature”.</p>

![a](https://user-images.githubusercontent.com/46979334/124638318-6f3dc080-de50-11eb-98da-6bd3cc725a3e.PNG)

![b](https://user-images.githubusercontent.com/46979334/124638383-811f6380-de50-11eb-8dee-0a27c2d4612a.PNG)


<h2>DATA CLEANING</h2>

Deleted “Celsius” from data frame

Having temperature measured in both Celsius and Fahrenheit seems redundant. So I removed the column by using the drop command and inserting ”Celsius’.


Changed column name “Fahrenheit” to “Temperature”

Assigned the new column names to variable new_column_names and then assigned that variable to the original columns to make the name change.

Notice this changes in the chart to the left in comparison to the chart above!

![C](https://user-images.githubusercontent.com/46979334/124638965-34885800-de51-11eb-8e83-47b8dc4368d3.PNG)

![D](https://user-images.githubusercontent.com/46979334/124638984-3baf6600-de51-11eb-9460-067335e6bf21.PNG)

# EXPLORATORY DATA ANALYSIS

Let’s get to “know” the data! Below are some highlights that will help us to better understand our data. 


![image](https://user-images.githubusercontent.com/46979334/124639296-9c3ea300-de51-11eb-8ac5-db9607c9b0d0.png)

![image](https://user-images.githubusercontent.com/46979334/124639405-bed0bc00-de51-11eb-9680-3c7f494f4008.png)

<h2>TEMPERATURE HISTOGRAM</h2>
I created a histogram  for the temperature using the matplotlib Python library. 

Each bar groups numbers into ranges. The graph displays the shape and spread of continuous sample data.The taller bars show that the largest amount of days in the data falls on the days where the temperature is between 70-80 degrees.

![image](https://user-images.githubusercontent.com/46979334/124639479-d445e600-de51-11eb-8b86-a40830f71229.png)


<h2>REVENUE HISTOGRAM</h2>
I created a histogram  for the Revenue using the matplotlib Python library. 

In this histogram, much like the other groups alike numbers in the data. The tallest bars show that the daily revenue was from about $400  to $600 on average.

![image](https://user-images.githubusercontent.com/46979334/124639556-ede72d80-de51-11eb-8c4f-9524213bb6b0.png)

<h2>Aggregate Temperature Ranges</h2>
SQL CASE query was used to round to nearest whole number and group temperatures together in increments of 10 degrees .

A pie chart and 100% Stacked Bar chart were created using the results of the SQL query. 

We can see that the largest percent of revenue (16.8%) comes from the days were the temperature was 110- 120, which is also the highest temperatures in the data

![image](https://user-images.githubusercontent.com/46979334/124639620-ff303a00-de51-11eb-9757-e68e6d5d69a5.png)

![CHART](https://user-images.githubusercontent.com/46979334/124639732-20912600-de52-11eb-9aff-5b9eb6502fb1.PNG)

![image](https://user-images.githubusercontent.com/46979334/124639751-27b83400-de52-11eb-9068-40ef1516e319.png)

![image](https://user-images.githubusercontent.com/46979334/124639778-2c7ce800-de52-11eb-9dc9-bc1847c5ea32.png)

<h2>LINEAR REGRESSION</h2>
Using Linear Regression, written in Python, we are able to see the relationship between revenue ($) and the temperature outside.

The result shows that there is a high positive correlation between the two. So we can forecast that as the temperature increases the amount of revenue follows suit.

![image](https://user-images.githubusercontent.com/46979334/124639821-3999d700-de52-11eb-8cde-ea06b053f7b9.png)

![image](https://user-images.githubusercontent.com/46979334/124639851-41597b80-de52-11eb-8280-7215b042710e.png)


<h2>TRAIN AND TEST MODEL</h2>
I split the data into train and test sets with a test size of 20%.

The regression score is 97.5%. Currently work on a user-end model that predicts sales revenue with 97.55% accuracy when temperature is input using this prediction model. 

![image](https://user-images.githubusercontent.com/46979334/124639908-559d7880-de52-11eb-97a4-e343bbc599a2.png)

![image](https://user-images.githubusercontent.com/46979334/124639938-5b935980-de52-11eb-87b2-9555f791576e.png)
![image](https://user-images.githubusercontent.com/46979334/124639956-60580d80-de52-11eb-9dcc-bf8dd0aac455.png)

![image](https://user-images.githubusercontent.com/46979334/124643706-00179a80-de57-11eb-8872-52429d380fb9.png)



# RESOURCES

<li>Python Version: 3.7</li>
<li>Python libraries: pandas, sklearn, matplotlib, seaborn</li>
<li>MySQL Version: 1.2.1</li>
<li>Microsoft Excel</li>
<li>Data set: Ice cream shop</li>

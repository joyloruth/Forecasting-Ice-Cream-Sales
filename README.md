# Forecasting-Ice-Cream-Sales
Using MySQL and Python, I split the data into train and test sets with a test size of 20% and am currently using this data to build a model that predicts sales revenue with 97.55% accuracy when the end-user inputs a temperature.




<h1> Forecasting Ice Cream Revenue</h1>
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

1.3.1 Remove Column
Deleted “Celsius” from data frame

Having temperature measured in both Celsius and Fahrenheit seems redundant. So I removed the column by using the drop command and inserting ”Celsius’.


Changed column name “Fahrenheit” to “Temperature”

Assigned the new column names to variable new_column_names and then assigned that variable to the original columns to make the name change.

Notice this changes in the chart to the left in comparison to the chart above!






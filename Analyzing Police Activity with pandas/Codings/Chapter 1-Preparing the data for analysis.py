# Exercise
# Examining the dataset
# Throughout this course, you'll be analyzing a dataset of traffic stops in Rhode Island that was collected by the Stanford Open Policing Project.

# Before beginning your analysis, it's important that you familiarize yourself with the dataset. In this exercise, you'll read the dataset into pandas, examine the first few rows, and then count the number of missing values.

# Instructions

# Import pandas using the alias pd.
# Read the file police.csv into a DataFrame named ri.
# Examine the first 5 rows of the DataFrame (known as the "head").
# Count the number of missing values in each column: Use .isnull() to check which DataFrame elements are missing, and then take the .sum() to count the number of True values in each column.

# Import the pandas library as pd
import pandas as pd

# Read 'police.csv' into a DataFrame named ri
ri = pd.read_csv('police.csv')

# Examine the head of the DataFrame
print(ri.head())

# Count the number of missing values in each column
print(ri.isnull().sum())

# Exercise
# Dropping columns
# Often, a DataFrame will contain columns that are not useful to your analysis. Such columns should be dropped from the DataFrame, to make it easier for you to focus on the remaining columns.

# In this exercise, you'll drop the county_name column because it only contains missing values, and you'll drop the state column because all of the traffic stops took place in one state (Rhode Island). Thus, these columns can be dropped because they contain no useful information.

# Instructions

# Count the number of missing values in each column. (This has been done for you.)
# Examine the DataFrame's .shape to find out the number of rows and columns.
# Drop both the county_name and state columns by passing the column names to the .drop() method as a list of strings.
# Examine the .shape again to verify that there are now two fewer columns.
# Count the number of missing values in each column
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Drop the 'county_name' and 'state' columns
ri.drop(['county_name' , 'state'], axis='columns', inplace=True)

# Examine the shape of the DataFrame (again)
print(ri.shape)

# Exercise
# Dropping rows
# When you know that a specific column will be critical to your analysis, and only a small fraction of rows are missing a value in that column, it often makes sense to remove those rows from the dataset.

# During this course, the driver_gender column will be critical to many of your analyses. Because only a small fraction of rows are missing driver_gender, we'll drop those rows from the dataset.


# Count the number of missing values in each column.
# Drop all rows that are missing driver_gender by passing the column name to the subset parameter of .dropna().
# Count the number of missing values in each column again, to verify that none of the remaining rows are missing driver_gender.
# Examine the DataFrame's .shape to see how many rows and columns remain.
# Count the number of missing values in each column
print(ri.isnull().sum())

# Drop all rows that are missing 'driver_gender'
ri.dropna(subset=['driver_gender'], inplace=True)

# Count the number of missing values in each column (again)
print(ri.isnull().sum())

# Examine the shape of the DataFrame
print(ri.shape)

# Exercise
# Fixing a data type
# We saw in the previous exercise that the is_arrested column currently has the object data type. In this exercise, we'll change the data type to bool, which is the most suitable type for a column containing True and False values.

# Fixing the data type will enable us to use mathematical operations on the is_arrested column that would not be possible otherwise.

# Instructions

# Examine the head of the is_arrested column to verify that it contains True and False values.
# Check the current data type of is_arrested.
# Use the .astype() method to convert is_arrested to a bool column.
# Check the new data type of is_arrested, to confirm that it is now a bool column.

# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Check the data type of 'is_arrested'
print(ri.is_arrested.dtype)

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype('bool')

# Check the data type of 'is_arrested' (again)
print(ri.is_arrested.dtype)

# Exercise
# Combining object columns
# Currently, the date and time of each traffic stop are stored in separate object columns: stop_date and stop_time.

# In this exercise, you'll combine these two columns into a single column, and then convert it to datetime format. This will enable convenient date-based attributes that we'll use later in the course.

# Instructions

# Use a string method to concatenate stop_date and stop_time (separated by a space), and store the result in combined.
# Convert combined to datetime format, and store the result in a new column named stop_datetime.
# Examine the DataFrame .dtypes to confirm that stop_datetime is a datetime column.
# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)

# Exercise
# Setting the index
# The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. By replacing the default index with a DatetimeIndex, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course!

# Instructions

# Set stop_datetime as the DataFrame index.
# Examine the index to verify that it is a DatetimeIndex.
# Examine the DataFrame columns to confirm that stop_datetime is no longer one of the columns.

# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)
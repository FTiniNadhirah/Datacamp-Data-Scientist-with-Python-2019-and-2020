# Exercise
# Calculating the hourly arrest rate
# When a police officer stops a driver, a small percentage of those stops ends in an arrest. This is known as the arrest rate. In this exercise, you'll find out whether the arrest rate varies by time of day.

# First, you'll calculate the arrest rate across all stops. Then, you'll calculate the hourly arrest rate by using the hour attribute of the index. The hour ranges from 0 to 23, in which:

# 0 = midnight
# 12 = noon
# 23 = 11 PM
# Instructions

# Take the mean of the is_arrested column to calculate the overall arrest rate.
# Group by the hour attribute of the DataFrame index to calculate the hourly arrest rate.
# Save the hourly arrest rate Series as a new object, hourly_arrest_rate.
# Calculate the overall arrest rate
print(ri.is_arrested.mean())

# Calculate the hourly arrest rate
print(ri.groupby(ri.index.hour).is_arrested.mean())

# Save the hourly arrest rate
hourly_arrest_rate = ri.groupby(ri.index.hour).is_arrested.mean()

# Exercise
# Plotting the hourly arrest rate
# In this exercise, you'll create a line plot from the hourly_arrest_rate object. A line plot is appropriate in this case because you're showing how a quantity changes over time.

# This plot should help you to spot some trends that may not have been obvious when examining the raw numbers!

# Instructions

# Import matplotlib.pyplot using the alias plt.
# Create a line plot of hourly_arrest_rate using the .plot() method.
# Label the x-axis as 'Hour', label the y-axis as 'Arrest Rate', and title the plot 'Arrest Rate by Time of Day'.
# Display the plot using the .show() function.
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Create a line plot of 'hourly_arrest_rate'
hourly_arrest_rate.plot()

# Add the xlabel, ylabel, and title
plt.xlabel('Hour')
plt.ylabel('Arrest Rate')
plt.title('Arrest Rate by Time of Day')

# Display the plot
plt.show()

# Exercise
# Plotting drug-related stops
# In a small portion of traffic stops, drugs are found in the vehicle during a search. In this exercise, you'll assess whether these drug-related stops are becoming more common over time.

# The Boolean column drugs_related_stop indicates whether drugs were found during a given stop. You'll calculate the annual drug rate by resampling this column, and then you'll use a line plot to visualize how the rate has changed over time.

# Instructions

# Calculate the annual rate of drug-related stops by resampling the drugs_related_stop column (on the 'A' frequency) and taking the mean.
# Save the annual drug rate Series as a new object, annual_drug_rate.
# Create a line plot of annual_drug_rate using the .plot() method.
# Display the plot using the .show() function.
# Calculate the annual rate of drug-related stops
print(ri.drugs_related_stop.resample('A').mean())

# Save the annual rate of drug-related stops
annual_drug_rate = ri.drugs_related_stop.resample('A').mean()

# Create a line plot of 'annual_drug_rate'
annual_drug_rate.plot()

# Display the plot
plt.show()

# Exercise
# Comparing drug and search rates
# As you saw in the last exercise, the rate of drug-related stops increased significantly between 2005 and 2015. You might hypothesize that the rate of vehicle searches was also increasing, which would have led to an increase in drug-related stops even if more drivers were not carrying drugs.

# You can test this hypothesis by calculating the annual search rate, and then plotting it against the annual drug rate. If the hypothesis is true, then you'll see both rates increasing over time.

# Instructions

# Calculate the annual search rate by resampling the search_conducted column, and save the result as annual_search_rate.
# Concatenate annual_drug_rate and annual_search_rate along the columns axis, and save the result as annual.
# Create subplots of the drug and search rates from the annual DataFrame.
# Display the subplots.

# Calculate and save the annual search rate
annual_search_rate = ri.search_conducted.resample('A').mean()

# Concatenate 'annual_drug_rate' and 'annual_search_rate'
annual = pd.concat([annual_drug_rate, annual_search_rate], axis='columns')

# Create subplots from 'annual'
annual.plot(subplots=True)

# Display the subplots
plt.show()

# Exercise
# Tallying violations by district
# The state of Rhode Island is broken into six police districts, also known as zones. How do the zones compare in terms of what violations are caught by police?

# In this exercise, you'll create a frequency table to determine how many violations of each type took place in each of the six zones. Then, you'll filter the table to focus on the "K" zones, which you'll examine further in the next exercise.

# Instructions

# Create a frequency table from the district and violation columns using the pd.crosstab() function.
# Save the frequency table as a new object, all_zones.
# Select rows 'Zone K1' through 'Zone K3' from all_zones using the .loc[] accessor.
# Save the smaller table as a new object, k_zones.
# Create a frequency table of districts and violations
print(pd.crosstab(ri.district, ri.violation))

# Save the frequency table as 'all_zones'
all_zones = pd.crosstab(ri.district, ri.violation)

# Select rows 'Zone K1' through 'Zone K3'
print(all_zones.loc['Zone K1':'Zone K3'])

# Save the smaller table as 'k_zones'
k_zones = all_zones.loc['Zone K1':'Zone K3']

# Exercise
# Plotting violations by district
# Now that you've created a frequency table focused on the "K" zones, you'll visualize the data to help you compare what violations are being caught in each zone.

# First you'll create a bar plot, which is an appropriate plot type since you're comparing categorical data. Then you'll create a stacked bar plot in order to get a slightly different look at the data. Which plot do you find to be more insightful?

# Instructions 1/2

# Create a bar plot of k_zones.
# Display the plot and examine it. What do you notice about each of the zones?
# Create a bar plot of 'k_zones'
k_zones.plot(kind='bar')

# Display the plot
plt.show()

# Instructions 2/2

# Create a stacked bar plot of k_zones.
# Display the plot and examine it. Do you notice anything different about the data than you did previously?
# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind='bar', stacked=True)

# Display the plot
plt.show()

# Exercise
# Converting stop durations to numbers
# In the traffic stops dataset, the stop_duration column tells you approximately how long the driver was detained by the officer. Unfortunately, the durations are stored as strings, such as '0-15 Min'. How can you make this data easier to analyze?

# In this exercise, you'll convert the stop durations to integers. Because the precise durations are not available, you'll have to estimate the numbers using reasonable values:

# Convert '0-15 Min' to 8
# Convert '16-30 Min' to 23
# Convert '30+ Min' to 45
# Instructions

# Print the unique values in the stop_duration column. (This has been done for you.)
# Create a dictionary called mapping that maps the stop_duration strings to the integers specified above.
# Convert the stop_duration strings to integers using the mapping, and store the results in a new column called stop_minutes.
# Print the unique values in the stop_minutes column, to verify that the durations were properly converted to integers.

# Print the unique values in 'stop_duration'
print(ri.stop_duration.unique())

# Create a dictionary that maps strings to integers
mapping = {'0-15 Min':8, '16-30 Min':23, '30+ Min':45}

# Convert the 'stop_duration' strings to integers using the 'mapping'
ri['stop_minutes'] = ri.stop_duration.map(mapping)

# Print the unique values in 'stop_minutes'
print(ri.stop_minutes.unique())

# Exercise
# Plotting stop length
# If you were stopped for a particular violation, how long might you expect to be detained?

# In this exercise, you'll visualize the average length of time drivers are stopped for each type of violation. Rather than using the violation column in this exercise, you'll use violation_raw since it contains more detailed descriptions of the violations.

# Instructions

# For each value in the violation_raw column, calculate the mean number of stop_minutes that a driver is detained.
# Save the resulting Series as a new object, stop_length.
# Sort stop_length by its values, and then visualize it using a horizontal bar plot.
# Display the plot.
# Calculate the mean 'stop_minutes' for each value in 'violation_raw'
print(ri.groupby('violation_raw').stop_minutes.mean())

# Save the resulting Series as 'stop_length'
stop_length = ri.groupby('violation_raw').stop_minutes.mean()

# Sort 'stop_length' by its values and create a horizontal bar plot
stop_length.sort_values().plot(kind='barh')

# Display the plot
plt.show()
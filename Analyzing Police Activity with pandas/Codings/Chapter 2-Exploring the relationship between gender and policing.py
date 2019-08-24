# Exercise
# Examining traffic violations
# Before comparing the violations being committed by each gender, you should examine the violations committed by all drivers to get a baseline understanding of the data.

# In this exercise, you'll count the unique values in the violation column, and then separately express those counts as proportions.

# Instructions

# Count the unique values in the violation column of the ri DataFrame, to see what violations are being committed by all drivers.
# Express the violation counts as proportions of the total.
# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))

# Exercise
# Comparing violations by gender
# The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.

# In this exercise, you'll first create a DataFrame for each gender, and then analyze the violations in each DataFrame separately.

# Instructions

# Create a DataFrame, female, that only contains rows in which driver_gender is 'F'.
# Create a DataFrame, male, that only contains rows in which driver_gender is 'M'.
# Count the violations committed by female drivers and express them as proportions.
# Count the violations committed by male drivers and express them as proportions.

# Create a DataFrame of female drivers
female = ri[ri.driver_gender == 'F']

# Create a DataFrame of male drivers
male = ri[ri.driver_gender == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize=True))

# Exercise
# Comparing speeding outcomes by gender
# When a driver is pulled over for speeding, many people believe that gender has an impact on whether the driver will receive a ticket or a warning. Can you find evidence of this in the dataset?

# First, you'll create two DataFrames of drivers who were stopped for speeding: one containing females and the other containing males.

# Then, for each gender, you'll use the stop_outcome column to calculate what percentage of stops resulted in a "Citation" (meaning a ticket) versus a "Warning".

# Instructions

# Create a DataFrame, female_and_speeding, that only includes female drivers who were stopped for speeding.
# Create a DataFrame, male_and_speeding, that only includes male drivers who were stopped for speeding.
# Count the stop outcomes for the female drivers and express them as proportions.
# Count the stop outcomes for the male drivers and express them as proportions.
# Create a DataFrame of female drivers stopped for speeding
female_and_speeding = ri[(ri.driver_gender == 'F') & (ri.violation == 'Speeding')]

# Create a DataFrame of male drivers stopped for speeding
male_and_speeding = ri[(ri.driver_gender == 'M') & (ri.violation == 'Speeding')]

# Compute the stop outcomes for female drivers (as proportions)
print(female_and_speeding.stop_outcome.value_counts(normalize=True))

# Compute the stop outcomes for male drivers (as proportions)
print(male_and_speeding.stop_outcome.value_counts(normalize=True))

# Exercise
# Calculating the search rate
# During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops that result in a vehicle search, also known as the search rate.

# Instructions

# Check the data type of search_conducted to confirm that it's a Boolean Series.
# Calculate the search rate by counting the Series values and expressing them as proportions.
# Calculate the search rate by taking the mean of the Series. (It should match the proportion of True values calculated above.)
# Check the data type of 'search_conducted'
print(ri.search_conducted.dtype)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())

# Exercise
# Comparing search rates by gender
# In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about 3.8%.

# First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a .groupby().

# Instructions 1/3

# Filter the DataFrame to only include female drivers, and then calculate the search rate by taking the mean of search_conducted.
# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())

# Instructions 2/3

# Filter the DataFrame to only include male drivers, and then repeat the search rate calculation.
# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())

# Instructions 3/3

# Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)
# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())

# Exercise
# Adding a second factor to the analysis
# Even though the search rate for males is much higher than for females, it's possible that the difference is mostly due to a second factor.

# For example, you might hypothesize that the search rate varies by violation type, and the difference in search rate between males and females is because they tend to commit different violations.

# You can test this hypothesis by examining the search rate for each combination of gender and violation. If the hypothesis was true, you would find that males and females are searched at about the same rate for each violation. Find out below if that's the case!

# Instructions 1/2

# Use a .groupby() to calculate the search rate for each combination of gender and violation. Are males and females searched at about the same rate for each violation?
# Calculate the search rate for each combination of gender and violation
print(ri.groupby(['driver_gender', 'violation']).search_conducted.mean())

# Instructions 2/2

# Reverse the ordering to group by violation before gender. The results may be easier to compare when presented this way.
# Reverse the ordering to group by violation before gender
print(ri.groupby(['violation', 'driver_gender']).search_conducted.mean())

# Exercise
# Counting protective frisks
# During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a "protective frisk."

# In this exercise, you'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.

# Instructions

# Count the search_type values to see how many times "Protective Frisk" was the only search type.
# Create a new column, frisk, that is True if search_type contains the string "Protective Frisk" and False otherwise.
# Check the data type of frisk to confirm that it's a Boolean Series.
# Take the sum of frisk to count the total number of frisks.
# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri.frisk.dtype)

# Take the sum of 'frisk'
print(ri.frisk.sum())

# Exercise
# Comparing frisk rates by gender
# In this exercise, you'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?

# Before doing any calculations, it's important to filter the DataFrame to only include the relevant subset of data, namely stops in which a search was conducted.

# Instructions

# Create a DataFrame, searched, that only contains rows in which search_conducted is True.
# Take the mean of the frisk column to find out what percentage of searches included a frisk.
# Calculate the frisk rate for each gender using a .groupby().
# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())

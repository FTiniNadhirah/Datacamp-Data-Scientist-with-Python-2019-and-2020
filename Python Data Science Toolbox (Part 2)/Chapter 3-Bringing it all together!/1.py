# Exercise
# Exercise
# Dictionaries for data science
# For this exercise, you'll use what you've learned about the zip() function and combine two lists into a dictionary.

# These lists are actually extracted from a bigger dataset file of world development indicators from the World Bank. For pedagogical purposes, we have pre-processed this dataset into the lists that you'll be working with.

# The first list feature_names contains header names of the dataset and the second list row_vals contains actual values of a row from the dataset, corresponding to each of the header names.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Create a zip object by calling zip() and passing to it feature_names and row_vals. Assign the result to zipped_lists.
# Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists. Assign the resulting dictionary to rs_dict.

# Zip lists: zipped_lists
zipped_lists = zip(feature_names, row_vals)
type(zipped_lists)

# Create a dictionary: rs_dict
rs_dict = dict(zipped_lists)
type(rs_dict)

# Print the dictionary
print(rs_dict)
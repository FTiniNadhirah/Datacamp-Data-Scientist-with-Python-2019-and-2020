# Exercise
# Importing flat files from the web: your turn!
# You are about to import your first file from the web! The flat file you will import will be 'winequality-red.csv' from the University of California, Irvine's Machine Learning repository. The flat file contains tabular data of physiochemical properties of red wine, such as pH, alcohol content and citric acid content, along with wine quality rating.

# The URL of the file is

# 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# After you import it, you'll check your working directory to confirm that it is there and then you'll load it into a pandas DataFrame.

# Instructions

# Import the function urlretrieve from the subpackage urllib.request.
# Assign the URL of the file to the variable url.
# Use the function urlretrieve() to save the file locally as 'winequality-red.csv'.
# Execute the remaining code to load 'winequality-red.csv' in a pandas DataFrame and to print its head to the shell.

from urllib.request import urlretrieve 

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url,'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# Exercise

# Opening and reading flat files from the web
# You have just imported a file from the web, saved it locally and loaded it into a DataFrame. If you just wanted to load a file from the web into a DataFrame without first saving it locally, you can do that easily using pandas. In particular, you can use the function pd.read_csv() with the URL as the first argument and the separator sep as the second argument.

# The URL of the file, once again, is

# 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Instructions

# Assign the URL of the file to the variable url.
# Read file into a DataFrame df using pd.read_csv(), recalling that the separator in the file is ';'.
# Print the head of the DataFrame df.
# Execute the rest of the code to plot histogram of the first feature in the DataFrame df.

import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Read file into a DataFrame: df
df = pd.read_csv(url, sep=';')

# Print the head of the DataFrame
print(df.head())

# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()





# Exercise
# Compatibility with different versions
# A common case for using environments is in developing scripts or Jupyter notebooks that rely on particular software versions for their functionality. Over time, the underlying tools might change, making updating the scripts worthwhile. Being able to switch between environments with different versions of the underlying packages installed makes this development process much easier.

# In this chapter, you will walk through steps of doing this with a very simple script as an example.

# Instructions 1/4
# The file weekly_humidity.py is stored in the current session. First just take a look at it using the Unix tool cat. You will see that the purpose of this script is rather trivial: it shows the last few days of the rolling mean of humidity taken from a data file. It would be easy to generalize this with switches to show different periods, different rolling intervals, different data sources, etc.
$ cat weekly_humidity.py

# Instructions 2/4
# Run the script (in the current base environment).
$ python weekly_humidity.py

# Instructions 3/4
# The script ran and produced a little report of the rolling mean of humidity. However, it also produced some rather noisy complaints about deprecated syntax in the Pandas library (called a FutureWarning). You now remember that you created this script a few years ago when you were using the pd-2015 environment. Switch to that environment.
$ conda activate pd-2015

# Instructions 4/4
# Run the script in the current pd-2015 environment. You will notice that the report itself is the same, but the FutureWarning is not present. For a first step, this is how to utilize this script.
$ python weekly_humidity.py

# Exercise
# Updating a script
# You certainly have the easy option to continue using the pd-2015 environment whenever you need to run the weekly_humidity.py script. Environments can be kept around as long as you like and will assure that all your old scripts (and notebooks, libraries, etc) continue to run the same way they always have.

# But quite likely you would like to update your script for your colleagues who use more recent versions of Python. Ideally, you would like them not to have to worry about this message:

# FutureWarning: pd.rolling_mean is deprecated for Series and will be removed in a future version, replace with 
     # Series.rolling(window=7,center=False).mean()
  # print(pd.rolling_mean(humidity, 7).tail(5))
# Happily, the warning itself pretty much tells you exactly how to update your script.

# Instructions 1/4
# Use the nano text editor to modify weekly_humidity.py so the last line is changed to:

# print(humidity.rolling(7).mean().tail(5))
# If you are more familiar with them, the editors vim and emacs are also installed in this session.
sed -i '$ d' weekly_humidity.py && echo 'print(humidity.rolling(7).mean().tail(5))' >> weekly_humidity.py


# Instructions 2/4
# Run the modified script in the active base environment that contains Panda 0.22. The FutureWarning should be gone now.
$ python weekly_humidity.py

# Instructions 3/4
# APIs do change over time. You should check whether your script, as modified, works in the older Pandas 0.17 installed in pd-2015. So, switch to the pd-2015 environment.
$ conda activate pd-2015

# Instructions 4/4
# Now, run the script in the current pd-2015 environment. You will notice that a new failure mode occurs now because Pandas 0.17 does not support the newer API you have used in your modified script.
$ python weekly_humidity.py
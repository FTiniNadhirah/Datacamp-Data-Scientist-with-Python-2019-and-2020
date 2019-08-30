# Exercise
# How can I print a variable's value?
# A simpler way to find a variable's value is to use a command called echo, which prints its arguments. Typing

# echo hello DataCamp!
# prints

# hello DataCamp!
# If you try to use it to print a variable's value like this:

# echo USER
# it will print the variable's name, USER.

# To get the variable's value, you must put a dollar sign $ in front of it. Typing

# echo $USER
# prints

# repl
# This is true everywhere: to get the value of a variable called X, you must write $X. (This is so that the shell can tell whether you mean "a file named X" or "the value of a variable named X".)

# Instructions

# The variable OSTYPE holds the name of the kind of operating system you are using. Display its value using echo.

$ echo $OSTYPE

# Exercise
# How else does the shell store information?
# The other kind of variable is called a shell variable, which is like a local variable in a programming language.

# To create a shell variable, you simply assign a value to a name:

# training=seasonal/summer.csv
# without any spaces before or after the = sign. Once you have done this, you can check the variable's value with:

# echo $training
# seasonal/summer.csv

# Instructions 1/2
# Define a variable called testing with the value seasonal/winter.csv.
$ testing=seasonal/winter.csv

# Instructions 2/2
# Use head -n 1 SOMETHING to get the first line from seasonal/winter.csv using the value of the variable testing instead of the name of the file.
$ head -n 1 $testing

# Exercise
# How can I repeat a command many times?
# Shell variables are also used in loops, which repeat commands many times. If we run this command:

# for filetype in gif jpg png; do echo $filetype; done
# it produces:

# gif
# jpg
# png
# Notice these things about the loop:

# The structure is for ...variable... in ...list... ; do ...body... ; done
# The list of things the loop is to process (in our case, the words gif, jpg, and png).
# The variable that keeps track of which thing the loop is currently processing (in our case, filetype).
# The body of the loop that does the processing (in our case, echo $filetype).
# Notice that the body uses $filetype to get the variable's value instead of just filetype, just like it does with any other shell variable. Also notice where the semi-colons go: the first one comes between the list and the keyword do, and the second comes between the body and the keyword done.

# Instructions

# Modify the loop so that it prints:

# docx
# odt
# pdf
# Please use filetype as the name of the loop variable.
$ for filetype in docx odt pdf; do echo $filetype; done

# Exercise
# How can I repeat a command once for each file?
# You can always type in the names of the files you want to process when writing the loop, but it's usually better to use wildcards. Try running this loop in the console:

# for filename in seasonal/*.csv; do echo $filename; done
# It prints:

# seasonal/autumn.csv
# seasonal/spring.csv
# seasonal/summer.csv
# seasonal/winter.csv
# because the shell expands seasonal/*.csv to be a list of four filenames before it runs the loop.

# Instructions

# Modify the wildcard expression to people/* so that the loop prints the names of the files in the people directory regardless of what suffix they do or don't have. Please use filename as the name of your loop variable.
$ for filename in people/*; do echo $filename; done

# Exercise
# How can I record the names of a set of files?
# People often set a variable using a wildcard expression to record a list of filenames. For example, if you define datasets like this:

# datasets=seasonal/*.csv
# you can display the files' names later using:

# for filename in $datasets; do echo $filename; done
# This saves typing and makes errors less likely.

# If you run these two commands in your home directory, how many lines of output will they print?

# files=seasonal/*.csv
# for f in $files; do echo $f; done

# Exercise
# How can I run many commands in a single loop?
# Printing filenames is useful for debugging, but the real purpose of loops is to do things with multiple files. This loop prints the second line of each data file:

# for file in seasonal/*.csv; do head -n 2 $file | tail -n 1; done
# It has the same structure as the other loops you have already seen: all that's different is that its body is a pipeline of two commands instead of a single command.

# Instructions

# Write a loop that produces the same output as

# grep -h 2017-07 seasonal/*.csv
# but uses a loop to process each file separately. Please use file as the name of the loop variable, and remember that the -h flag used above tells grep not to print filenames in the output.
$ for file in seasonal/*.csv; do grep 2017-07 $file; done
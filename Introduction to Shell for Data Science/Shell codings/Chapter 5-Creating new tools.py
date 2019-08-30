# Exercise
# How can I edit a file?
# Unix has a bewildering variety of text editors. For this course, we will use a simple one called Nano. If you type nano filename, it will open filename for editing (or create it if it doesn't already exist). You can move around with the arrow keys, delete characters using backspace, and do other operations with control-key combinations:

# Ctrl + K: delete a line.
# Ctrl + U: un-delete a line.
# Ctrl + O: save the file ('O' stands for 'output').
# Ctrl + X: exit the editor.

# Instructions

# Run nano names.txt to edit a new file in your home directory and enter the following four lines:

# Lovelace
# Hopper
# Johnson
# Wilson
# To save what you have written, type Ctrl + O to write the file out, then Enter to confirm the filename, then Ctrl + X and Enter to exit the editor.
$ cp /solutions/names.txt /home/repl

# Exercise
# How can I record what I just did?
# When you are doing a complex analysis, you will often want to keep a record of the commands you used. You can do this with the tools you have already seen:

# Run history.
# Pipe its output to tail -n 10 (or however many recent steps you want to save).
# Redirect that to a file called something like figure-5.history.
# This is better than writing things down in a lab notebook because it is guaranteed not to miss any steps. It also illustrates the central idea of the shell: simple tools that produce and consume lines of text can be combined in a wide variety of ways to solve a broad range of problems.

# Instructions 1/3
# Copy the files seasonal/spring.csv and seasonal/summer.csv to your home directory.
$ cp seasonal/s* ~

# Instructions 2/3
# Use grep with the -h flag (to stop it from printing filenames) and -v Tooth (to select lines that don't match the header line) to select the data records from spring.csv and summer.csv in that order and redirect the output to temp.csv.
$ grep -h -v Tooth spring.csv summer.csv > temp.csv

# Instructions 3/3
# Pipe history into tail -n 3 and redirect the output to steps.txt to save the last three commands in a file. (You need to save three instead of just two because the history command itself will be in the list.)
$ history | tail -n 3 > steps.txt

# Exercise
# How can I save commands to re-run later?
# You have been using the shell interactively so far. But since the commands you type in are just text, you can store them in files for the shell to run over and over again. To start exploring this powerful capability, put the following command in a file called headers.sh:

# head -n 1 seasonal/*.csv
# This command selects the first row from each of the CSV files in the seasonal directory. Once you have created this file, you can run it by typing:

# bash headers.sh
# This tells the shell (which is just a program called bash) to run the commands contained in the file headers.sh, which produces the same output as running the commands directly.

# Instructions 1/2
# Use nano dates.sh to create a file called dates.sh that contains this command:
$ cp /solutions/dates.sh .

# cut -d , -f 1 seasonal/*.csv
# to extract the first column from all of the CSV files in seasonal.

# Instructions 2/2
# Use bash to run the file dates.sh.
$ bash dates.sh

# Exercise
# How can I re-use pipes?
# A file full of shell commands is called a *shell script, or sometimes just a "script" for short. Scripts don't have to have names ending in .sh, but this lesson will use that convention to help you keep track of which files are scripts.

# Scripts can also contain pipes. For example, if all-dates.sh contains this line:

# cut -d , -f 1 seasonal/*.csv | grep -v Date | sort | uniq
# then:

# bash all-dates.sh > dates.out
# will extract the unique dates from the seasonal data files and save them in dates.out.

# Instructions 1/3
# A file teeth.sh in your home directory has been prepared for you, but contains some blanks. Use Nano to edit the file and replace the two ____ placeholders with seasonal/*.csv and -c so that this script prints a count of the number of times each tooth name appears in the CSV files in the seasonal directory.
$ cp /solutions/teeth.sh .

# Instructions 2/3
# Use bash to run teeth.sh and > to redirect its output to teeth.out.
$ bash teeth.sh > teeth.out

# Instructions 3/3
# Run cat teeth.out to inspect your results.
$ cat teeth.out

# Exercise
# How can I pass filenames to scripts?
# A script that processes specific files is useful as a record of what you did, but one that allows you to process any files you want is more useful. To support this, you can use the special expression $@ (dollar sign immediately followed by at-sign) to mean "all of the command-line parameters given to the script". For example, if unique-lines.sh contains this:

# sort $@ | uniq
# then when you run:

# bash unique-lines.sh seasonal/summer.csv
# the shell replaces $@ with seasonal/summer.csv and processes one file. If you run this:

# bash unique-lines.sh seasonal/summer.csv seasonal/autumn.csv
# it processes two data files, and so on.

# Instructions 1/2
# Edit the script count-records.sh with Nano and fill in the two ____ placeholders with $@ and -l respectively so that it counts the number of lines in one or more files, excluding the first line of each.
$ cp /solutions/count-records.sh .

# Instructions 2/2
# Run count-records.sh on seasonal/*.csv and redirect the output to num-records.out using >.
$ bash count-records.sh seasonal/*.csv > num-records.out

# Exercise
# How can one shell script do many things?
# Our shells scripts so far have had a single command or pipe, but a script can contain many lines of commands. For example, you can create one that tells you how many records are in the shortest and longest of your data files, i.e., the range of your datasets' lengths.

# Note that in Nano, "copy and paste" is achieved by navigating to the line you want to copy, pressing CTRL + K to cut the line, then CTRL + U twice to paste two copies of it.

# Instructions 1/4
# Use Nano to edit the script range.sh and replace the two ____ placeholders with $@ and -v so that it lists the names and number of lines in all of the files given on the command line without showing the total number of lines in all files. (Do not try to subtract the column header lines from the files.)
$ cp /solutions/range-1.sh range.sh

# Instructions 2/4
# Add sort -n and head -n 1 in that order to the pipeline in range.sh to display the name and line count of the shortest file given to it.
$ cp /solutions/range-2.sh range.sh

# Instructions 3/4
# Add a second line to range.sh to print the name and record count of the longest file in the directory as well as the shortest. This line should be a duplicate of the one you have already written, but with sort -n -r rather than sort -n.
$ cp /solutions/range-3.sh range.sh

# Instructions 4/4
# Run the script on the files in the seasonal directory using seasonal/*.csv to match all of the files and redirect the output using > to a file called range.out in your home directory.
$ bash range.sh seasonal/*.csv > range.out

# Exercise
# How can I write loops in a shell script?
# Shell scripts can also contain loops. You can write them using semi-colons, or split them across lines without semi-colons to make them more readable:

# # Print the first and last data records of each file.
# for filename in $@
# do
    # head -n 2 $filename | tail -n 1
    # tail -n 1 $filename
# done
# (You don't have to indent the commands inside the loop, but doing so makes things clearer.)

# The first line of this script is a comment to tell readers what the script does. Comments start with the # character and run to the end of the line. Your future self will thank you for adding brief explanations like the one shown here to every script you write.

# Instructions 1/3
# Fill in the placeholders in the script date-range.sh with $filename (twice), head, and tail so that it prints the first and last date from one or more files.
$ cp /solutions/date-range.sh date-range.sh

# Instructions 2/3
# Run date-range.sh on all four of the seasonal data files using seasonal/*.csv to match their names.
$ bash date-range.sh seasonal/*.csv

# Instructions 3/3
# Run date-range.sh on all four of the seasonal data files using seasonal/*.csv to match their names, and pipe its output to sort to see that your scripts can be used just like Unix's built-in commands.
$ bash date-range.sh seasonal/*.csv | sort

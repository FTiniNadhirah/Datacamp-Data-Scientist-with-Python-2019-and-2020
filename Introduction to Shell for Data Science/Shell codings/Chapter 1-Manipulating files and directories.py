# Exercise
# How else can I identify files and directories?
# An absolute path is like a latitude and longitude: it has the same value no matter where you are. A relative path, on the other hand, specifies a location starting from where you are: it's like saying "20 kilometers north".

# For example, if you are in the directory /home/repl, the relative path seasonal specifies the same directory as /home/repl/seasonal, while seasonal/winter.csv specifies the same file as /home/repl/seasonal/winter.csv. The shell decides if a path is absolute or relative by looking at its first character: if it begins with /, it is absolute, and if it doesn't, it is relative.

# Instructions 1/3
# You are in /home/repl. Use ls with a relative path to list the file /home/repl/course.txt (and only that file).

$ ls course.txt

# Instructions 2/3
# You are in /home/repl. Use ls with a relative path to list the file /home/repl/seasonal/summer.csv (and only that file).

$ ls seasonal/summer.csv


# Instructions 3/3
# You are in /home/repl. Use ls with a relative path to list the contents of the directory /home/repl/people.

$ ls people

# Exercise
# How can I move to another directory?
# Just as you can move around in a file browser by double-clicking on folders, you can move around in the filesystem using the command cd (which stands for "change directory").

# If you type cd seasonal and then type pwd, the shell will tell you that you are now in /home/repl/seasonal. If you then run ls on its own, it shows you the contents of /home/repl/seasonal, because that's where you are. If you want to get back to your home directory /home/repl, you can use the command cd /home/repl.

# Instructions 1/3
$ cd seasonal$ pwd


# Instructions 2/3
# Use pwd to check that you're there.
$ pwd

# Instructions 3/3

# Use ls without any paths to see what's in that directory.
$ ls

# Exercise
# How can I copy files?
# You will often want to copy files, move them into other directories to organize them, or rename them. One command to do this is cp, which is short for "copy". If original.txt is an existing file, then:

# cp original.txt duplicate.txt
# creates a copy of original.txt called duplicate.txt. If there already was a file called duplicate.txt, it is overwritten. If the last parameter to cp is an existing directory, then a command like:

# cp seasonal/autumn.csv seasonal/winter.csv backup
# copies all of the files into that directory.

# Instructions 1/2
# Make a copy of seasonal/summer.csv in the backup directory (which is also in /home/repl), calling the new file summer.bck.
$ cp seasonal/summer.csv backup/summer.bck

# # Instructions 2/2
# Copy spring.csv and summer.csv from the seasonal directory into the backup directory without changing your current working directory (/home/repl).
$ cp seasonal/spring.csv seasonal/summer.csv backup

# Exercise
# How can I move a file?
# While cp copies a file, mv moves it from one directory to another, just as if you had dragged it in a graphical file browser. It handles its parameters the same way as cp, so the command:

# mv autumn.csv winter.csv ..
# moves the files autumn.csv and winter.csv from the current working directory up one level to its parent directory (because .. always refers to the directory above your current location).

# Instructions

# You are in /home/repl, which has sub-directories seasonal and backup. Using a single command, move spring.csv and summer.csv from seasonal to backup.
$ mv seasonal/spring.csv seasonal/summer.csv backup

# Exercise
# How can I rename files?
# mv can also be used to rename files. If you run:

# mv course.txt old-course.txt
# then the file course.txt in the current working directory is "moved" to the file old-course.txt. This is different from the way file browsers work, but is often handy.

# One warning: just like cp, mv will overwrite existing files. If, for example, you already have a file called old-course.txt, then the command shown above will replace it with whatever is in course.txt.

# Instructions 1/3
# Go into the seasonal directory.
$ cd seasonal


# Instructions 2/3
# Rename the file winter.csv to be winter.csv.bck.
$ mv winter.csv winter.csv.bck

# Instructions 3/3
# Run ls to check that everything has worked.
$ ls

# Exercise
# How can I delete files?
# We can copy files and move them around; to delete them, we use rm, which stands for "remove". As with cp and mv, you can give rm the names of as many files as you'd like, so:

# rm thesis.txt backup/thesis-2017-08.txt
# removes both thesis.txt and backup/thesis-2017-08.txt

# rm does exactly what its name says, and it does it right away: unlike graphical file browsers, the shell doesn't have a trash can, so when you type the command above, your thesis is gone for good.

# Instructions 1/4

# You are in /home/repl. Go into the seasonal directory.
$ cd /home/repl/seasonal$ rm autumn.csv

# Instructions 2/4
# Remove autumn.csv.
$ pwd

# Instructions 3/4
# Go back to your home directory.
$ cd ..

# Instructions 4/4
# Remove seasonal/summer.csv without changing directories again.
$ rm seasonal/summer.csv

# Exercise
# How can I create and delete directories?
# mv treats directories the same way it treats files: if you are in your home directory and run mv seasonal by-season, for example, mv changes the name of the seasonal directory to by-season. However, rm works differently.

# If you try to rm a directory, the shell prints an error message telling you it can't do that, primarily to stop you from accidentally deleting an entire directory full of work. Instead, you can use a separate command called rmdir. For added safety, it only works when the directory is empty, so you must delete the files in a directory before you delete the directory. (Experienced users can use the -r option to rm to get the same effect; we will discuss command options in the next chapter.)

# Instructions 1/4
# Without changing directories, delete the file agarwal.txt in the people directory.
$ rm people/agarwal.txt$ rmdir

# Instructions 2/4
# Now that the people directory is empty, use a single command to delete it.
$ rmdir people

# Instructions 3/4
# Since a directory is not a file, you must use the command mkdir directory_name to create a new (empty) directory. Use this command to create a new directory called yearly below your home directory.
$ mkdir yearly

# Instructions 4/4
# Now that yearly exists, create another directory called 2017 inside it without leaving your home directory.
$ mkdir yearly/2017

# Exercise
# Wrapping up
# You will often create intermediate files when analyzing data. Rather than storing them in your home directory, you can put them in /tmp, which is where people and programs often keep files they only need briefly. (Note that /tmp is immediately below the root directory /, not below your home directory.) This wrap-up exercise will show you how to do that.

# Instructions 1/4
# Use cd to go into /tmp.
$ cd /tmp
# Instructions 2/4
# List the contents of /tmp without typing a directory name.
$ ls

# Instructions 3/4
# Make a new directory inside /tmp called scratch.
$ mkdir /tmp/scratch

# Instructions 4/4
# Move /home/repl/people/agarwal.txt into /tmp/scratch. We suggest you use the ~ shortcut for your home directory and a relative path for the second rather than the absolute path.
$ mv ~/people/agarwal.txt scratch


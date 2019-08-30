# Exercise
# Installing from a channel
# We saw in the last exercise that there are about 30,000 linux-64 packages on conda-forge. Across all the channels there are about 50,000 packages, most of those for at least 3 of of the 5 main platforms (osx-64, linux-32, linux-64, win-32, win-64; 32-bit support is of diminishing importance compared to 64-bit). There are around 2500 channels that have been active in the last 6 months; most are individual users, but a fair number belonging to projects or organizations. A majority of package names are published by more than one different channel; sometimes just as a copy, other times with a tweak or compiler optimization, or in a different version.

# The whole point of having channels is to be able to install packages from them. For this exercise, you will install a version of a package not available on the default channel. Adding a channel to install from simply requires using the same --channel or -c switch we have seen in other conda commands, but with the conda install command.

# For example:

# conda install --channel my-organization the-package
# Instructions 1/2
# A package named youtube-dl exists on conda-forge but is not available on the default channel. Please install it.
$ conda install -c conda-forge youtube-dl -y --no-deps

# Instructions 2/2
# You should examine what software is installed in your current environment now. You should notice that unlike other packages, the newly install youtube-dl came from a non-default channel.
$ conda list
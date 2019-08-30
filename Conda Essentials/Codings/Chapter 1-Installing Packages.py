# Exercise
# What version of conda do I have?
# The tool conda takes a variety of commands and arguments. Most of the time, you will use conda COMMAND OPTIONS --SWITCH. You will learn the collection of COMMANDs available in the next lessons. A summary is available on the help screen:

# $ conda --help
# usage: conda [-h] [-V] command ...

# conda is a tool for managing and deploying applications, environments and packages.

# Options:

# positional arguments:
  # command
    # clean        Remove unused packages and caches.
    # config       Modify configuration values in .condarc. This is modeled
                 # after the git config command. Writes to the user .condarc
                 # file (/Users/dmertz/.condarc) by default.
    # create       Create a new conda environment from a list of specified
                 # packages.
    # help         Displays a list of available conda commands and their help
                 # strings.
    # info         Display information about current conda install.
    # install      Installs a list of packages into a specified conda
                 # environment.
    # [... more commands ...]

# optional arguments:
  # -h, --help     Show this help message and exit.
  # -V, --version  Show the conda version number and exit.
# Instructions

# Run a command to determine what version of conda you have installed.
$ conda --version

# Exercise
# Install a conda package (II)
# Installing a package is largely a matter of listing the name(s) of packages to install after the command conda install. But there is more to it behind the scenes. The versions of packages to install (along with all their dependencies) must be compatible with all versions of other software currently installed. Often this "satisfiability" constraint depends on choosing a package version compatible with a particular version of Python that is installed. Conda is special among "package managers" in that it always guarantees this consistency; you will see the phrase "Solving environment..." during installation to indicate this computation.

# For example, you may simply instruct conda to install foo-lib. The tool first determines which operating system you are running, and then narrows the match to candidates made for this platform. Then, conda determines the version of Python on the system (say 3.7), and chooses the package version for -py37. But, beyond those simple limits, all dependencies are checked.

# Suppose foo-lib is available in versions 1.0, 1.1, 1.2, 2.0, 2.1, 2.2, 2.3, 3.0, 3.1 (for your platform and Python version). As a first goal, conda attempts to choose the latest version of foo-lib. However, maybe foo-lib depends on bar-lib, which itself is available in various versions (say 1 through 20 in its versioning scheme). It might be that foo-lib 3.1 is compatible with bar-lib versions 17, 18, and 19; but blob-lib (which is already installed) is compatible only with versions of bar-lib less than 17. Therefore, conda would examine the compatibility of foo-lib 3.0 as a fallback. In this hypothetical, foo-lib 3.0 is compatible with bar-lib 16, so that version is chosen (bar-lib is also updated to the latest compatible version 16 in the same command if an earlier version is currently installed).

# Visually (octagons mark chosen versions):

# Instructions

# Install the package cytoolz using conda. (Press y when asked to proceed.)
$ conda install cytoolz

# Exercise
# Install a specific version of a package (I)
# Sometimes there are reasons why you need to use a specific version of a package, not necessarily simply the latest version compatible with your other installed software. You may have scripts written that depend on particular older APIs, or you may have received code written by colleagues who used specific versions and you want to guarantee replication of the same behavior. Likewise, you may be writing code that you intend to pass to other users who you know to be using specific package versions on their systems (perhaps as a company standard, for example).

# conda allows you to install software versions in several flexible ways. Your most common pattern will probably be prefix notation, using semantic versioning. For example, you might want a MAJOR and MINOR version, but want conda to select the most up-to-date PATCH version within that series. You could spell that as:

# conda install foo-lib=12.3
# Or similarly, you may want a particular major version, and prefer conda to select the latest compatible MINOR version as well as PATCH level. You could spell that as:

# conda install foo-lib=13
# If you want to narrow the installation down to an exact PATCH level, you can specify that as well with:

# conda install foo-lib=14.3.2
# Keep in mind that relaxing constraints may allow for satisfying multiple dependencies among installed software. Occasionally you will try to install some software version that is simply inconsistent with other software installed, and conda will warn you about that rather than install anything.

# Instructions
# Install the module attrs in the specific MAJOR and MINOR version 17.3.
$ conda install attrs=17.3 --yes

# Exercise
# Update a conda package
# Closely related to installing a particular version of a conda package is updating the installed version to the latest version possible that remains compatible with other installed software. conda will determine if it is possible to update dependencies of the package(s) you are directly updating, and do so if resolvable. At times, the single specified package will be updated exclusively since the current dependencies are correct for the new version. Obviously, at other times updating will do nothing because you are already at the latest version possible.

# The command conda update PKGNAME is used to perform updates. Update is somewhat less "aggressive" than install in the sense that installing a specific (later) version will revise the versions in the dependency tree to a greater extent than an update. Often update will simply choose a later PATCH version even though potentially a later MAJOR or MINOR version could be made compatible with other installed packages.

# Note that this conda command, as well as most others allow specification of multiple packages on the same line. For example, you might use:

# conda update foo bar blob
# To bring all of foo, bar, and blob up to the latest compatible versions mutually satisfiable.

# Instructions

# The package pandas is installed in the current image, but it's not the most recent version. Update it.
$ conda update pandas

# Exercise
# Remove a conda package
# Finally, in direct package management, sometimes you want to remove a package. This is straightforward using the command conda remove PKGNAME. As with other commands, you may also optionally specify multiple packages separated by spaces.

# Note that conda always tries to use the most recent versions of installed software that are compatible. Therefore, sometimes removing one package allows another package to be upgraded implicitly because only the removed package was requiring the older version of the dependency.

# Instructions

# Remove the package pandas using conda.
$ conda remove pandas -y

# Exercise
# Search for available package versions?
# Sometimes you want to see what versions of a package are available as conda packages. By default conda search looks for those matching your platform (although switches allow tweaking this behavior).

# Instructions

# Check what versions of attrs are available on the current platform.
$ conda search attrs


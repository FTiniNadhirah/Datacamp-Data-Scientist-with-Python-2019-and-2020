# Exercise
# Switch between environments
# Simply having different environments is not of much use; you need to be able to switch between environments. Most typically this is done at the command line, using the conda command. With some other interfaces (like Anaconda Navigator or Jupyter with nb_conda installed), other techniques for selecting environment are available. But for this course, you will learn about command-line use.

# To activate an environment, you simply use conda activate ENVNAME. To deactivate an environment, you use conda deactivate, which returns you to the root/base environment.

# If you used conda outside this course, and prior to version 4.4, you may have seen a more platform specific style. On older versions, Windows users would type activate ENVNAME and deactivate, while Linux and OSX users would type source activate ENVNAME and source deactivate. The unified style across platforms is more friendly. Related to the change to conda activate, version 4.4 and above use a special environment called base that is equivalent to what was called root in older versions. However, in old versions of conda you would not typically see an environment listed on the terminal prompt when you were in the root environment.

# Instructions 1/3
# Activate the environment called course-env in the current session.
$ conda activate course-env

# Instructions 2/3
# Suppose you did some work within the course-env environment. Now you wish to utilize another environment. Activate the environment called pd-2015 in the current session.
$ conda activate pd-2015

# Instructions 3/3
# Deactivate the current environment you switched in the last step. This will bring you back to the base environment.
$ conda deactivate

# Exercise
# Remove an environment
# From time to time, it is worth cleaning up the environments you have accumulated just to make management easier. Doing so is not pressing; as they use little space or resources. But it's definitely useful to be able to see a list of only as many environments as are actually useful for you.

# The command to remove an environment is:

# conda env remove --name ENVNAME
# You may also use the shorter -n switch instead.

# Instructions
# The current session has an environment named deprecated. Remove it from the session.
$ conda env remove --name deprecated

# Exercise
# Create a new environment
# This course is configured with several environments, but in your use you will need to create environments meeting your own purposes. The basic command for creating environments is conda create. You will always need to specify a name for your environment, using --name (or short form -n), and you may optionally specify packages (with optional versions) that you want in that environment initially. You do not need to specify any packages when creating; either way you can add or remove whatever packages you wish from an environment later.

# The general syntax is similar to:

# conda create --name recent-pd python=3.6 pandas=0.22 scipy statsmodels
# This command will perform consistency resolution on those packages and versions indicated, in the same manner as a conda install will. Notice that even though this command works with environments it is conda create rather than a conda env ... command.

# Instructions 1/3
# Create a new environment called conda-essentials that contains attrs version 19.1.0 and the best available version of cytoolz (we pick these examples for illustration largely because they are small and have few dependencies).
$ conda create --name conda-essentials attrs=19.1.0 cytoolz -y

# Instructions 2/3
# Switch into the environment you just created named conda-essentials.
$ conda activate conda-essentials

# Instructions 3/3
# Examine all the software packages installed in the current conda-essentials environment.
$ conda list

# Exercise
# Export an environment
# Using conda list provides useful information about the packages that are installed. However, the format it describes packages in is not immediately usable to let a colleague or yourself to recreate exactly the same environment on a different machine. For that you want the conda env export command.

# There are several optional switches to this command. If you specify -n or --name you can export an environment other than the active one. Without that switch it chooses the active environment. If you specify -f or --file you can output the environment specification to a file rather than just to the terminal output. If you are familiar with piping, you might prefer to pipe the output to a file rather than use the --file switch. By convention, the name environment.yml is used for environment, but any name can be used (but the extension .yml is strongly encouraged).

# Without saving to a file, the output might look similar to the below. Notice that this gives exact versions of packages, not simply ranges or prefixes. This assures exact reproducibility of computation within the same environment on a different machine.

# $ conda env export -n pd-2015
# name: pd-2015
# channels:
  # - defaults
# dependencies:
  # - certifi=2018.1.18=py35_0
  # - libffi=3.2.1=hd88cf55_4
  # - libgcc-ng=7.2.0=h7cc24e2_2
  # - libgfortran-ng=7.2.0=h9f7466a_2
  # - mkl=2018.0.1=h19d6760_4
  # - numpy=1.9.3=py35hff6eb55_3
  # - openssl=1.0.2n=hb7f436b_0
  # - pandas=0.17.1=np19py35_0
  # - pip=9.0.1=py35h7e7da9d_4
  # - python=3.5.4=h417fded_24
  # - python-dateutil=2.6.1=py35h90d5b31_1
  # - pytz=2017.3=py35hb13c558_0
  # - readline=7.0=ha6073c6_4
  # - setuptools=38.4.0=py35_0
  # - six=1.11.0=py35h423b573_1
  # - xz=5.2.3=h55aa19d_2
  # - zlib=1.2.11=ha838bed_2
  # - pip:
    # - chardet==3.0.4
    # - pexpect==4.2.1
    # - urllib3==1.22
# prefix: /home/repl/miniconda/envs/pd-2015
# Instructions

# Export the environment called course-env to the file course-env.yml.
$ conda env export --name course-env --file course-env.yml

# Exercise
# Create an environment from a shared specification
# You may recreate an environment from one of the YAML (Yet Another Markup Language) format files produced by conda env export. However, it is also easy to hand write an environment specification with less detail. For example, you might describe an environment you need and want to share with colleagues as follows:

# $ cat shared-project.yml
# name: shared-project
# channels:
  # - defaults
# dependencies:
  # - python=3.6
  # - pandas>=0.21
  # - scikit-learn
  # - statsmodels
# Clearly this version is much less specific than what conda env export produces. But it indicates the general tools, with some version specification, that will be required to work on a shared project. Actually creating an environment from this sketched out specification will fill in all the dependencies of those large projects whose packages are named, and this will install dozens of packages not explicitly listed. Often you are happy to have other dependencies in the manner conda decides is best.

# Of course, a fully fleshed out specification like we saw in the previous exercise are equally usable. Non-relevant details like the path to the environment on the local system are ignored when installing to a different machine or to a different platform altogether, which will work equally well.

# To create an environment from file-name.yml, you can use the following command:

# conda env create --file file-name.yml
# As a special convention, if you use the plain command conda env create without specifying a YAML file, it will assume you mean the file environment.yml that lives in the local directory.

# Instructions 1/2
# A file environment.yml exists in the local directory within the current session. Use this file to create an environment called shared-project.
$ cat environment.yml

# Instructions 2/2
# The current session directory also has a file named shared-config.yml. Create an environment based on this specification. The name of this environment will be functional-data.
$ conda env create -f shared-config.yml
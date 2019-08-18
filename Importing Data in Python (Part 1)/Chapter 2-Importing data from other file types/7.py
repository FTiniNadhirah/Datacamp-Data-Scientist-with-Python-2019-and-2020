# Using h5py to import HDF5 files
# The file 'LIGO_data.hdf5' is already in your working directory. In this exercise, you'll import it using the h5py library. You'll also print out its datatype to confirm you have imported it correctly. You'll then study the structure of the file in order to see precisely what HDF groups it contains.

# You can find the LIGO data plus loads of documentation and tutorials here. There is also a great tutorial on Signal Processing with the data here.

# Instructions
# 100 XP
# Instructions
# 100 XP
# Import the package h5py.
# Assign the name of the file to the variable file.
# Load the file as read only into the variable data.
# Print the datatype of data.
# Print the names of the groups in the HDF5 file 'LIGO_data.hdf5'.

# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
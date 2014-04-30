import os
from os import listdir
from os.path import isfile, join

#python get all .txt files in a directory
#python get all txt files directory
#python find all text files in a folder

#Method 1
mypath = "C:\Files_To_Read"
#only_files = [ file for file in listdir(mypath) if isfile(join(mypath,file)) ]

only_files = []
for file in listdir(mypath):
    if isfile(join(mypath,file)) and file.endswith(".txt"):
        only_files.append(file)

print "\n" , only_files

#Method 2 using Glob
import glob
print "\n" , glob.glob("C:\Files_To_Read\*.txt")
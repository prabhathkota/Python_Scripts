import glob

"""
arr_list = glob.glob("C:\Prabhath\Technical\Python\Python_Scripts\Exercise\*.*")

for each_file in arr_list:
    print("Each File: ", each_file)
"""
"""
for each_file in listdir(mypath):
    if isfile(join(mypath,each_file))
        print()


from os import listdir
from os.path import isfile, join

mypath = 'C:\Prabhath\Technical\Python\Python_Scripts\Exercise'

#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

for each_file in listdir(mypath):
    print("Each File :", each_file)

#print("Only Files : ", onlyfiles)
"""

import os
rootdir = 'C:\Prabhath\Technical\Python\Python_Scripts\Exercise'

for subdir, dirs, files in os.walk(rootdir):
    print("\nSubdir :", subdir)
    print("dirs   :", dirs)
    for file in files:
        print("Each File ELSE: ", subdir + '\\' + file)

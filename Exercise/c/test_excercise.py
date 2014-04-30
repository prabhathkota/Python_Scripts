#How to Execute :
#python test_exercise.py main.txt

import sys
d={}  #Declaring dict
for line in open("lookup.txt"):
    line = line.strip().split("|")
    #print(line[-1])           #Last Element
    d[line[0]] = line[-1]      #Praparing Dict
for line in open(sys.argv[1]): #This file main.txt is being taken from command line "python test_exercise.py main.txt"
    if line.startswith('P'):
        print(line, end="")
    if line.startswith('T'):
        print(line, end="")
    if line.startswith('R'):
        line = line.strip().split("|")
        print('|'.join(line[0:3]) + '|' + d[line[3]] + '|' + '|'. join(line[4:]))


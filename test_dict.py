relatives  = {"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother", "Homer" : "father", "Santa" : "dog"}


#raw_input(), print for Python 2.X Version 
#input(), print() for Python 3.X Version

for member in sorted(relatives.keys()):
    #print "\n",member
    print member

print ""

for member in sorted(relatives.values()):
    #print "\n",member
    print member

print ""

for key, val in relatives.iteritems(): 
    #print "\n",member
    print key, val
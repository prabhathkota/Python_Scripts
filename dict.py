relatives = {"Lisa" : "daughter", "Bart" : "son", "Marge" : "mother", "Homer" : "father", "Santa" : "dog"}

#Keys are unique

relatives['Marge'] = "mother";		
relatives['marge'] = "mother1";

#'Marge' and 'marge' are different keys

for member in sorted(relatives.keys()):
    print("\n",member, "=>", relatives[member])
	#print "\n",member

for member in sorted(relatives.values()):
    print("\n",member)	
	#print "\n",member
	
for key, value in relatives.items():
	print("\n", key, "=>", value)
	#print "\n", key, "=>", value	
	
 	
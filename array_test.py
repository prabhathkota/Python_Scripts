'''
Created on Sep 12, 2013

@author: 521051
'''
arr1 = (10, 20, 30, 40, 50)
print len(arr1)
#U can't assign a new element
#arr1[5] = 60   
print len(arr1)

#List
arr1 = [10, 20, 30, 40, 50]
print arr1  
#You can't assign out of index range
#arr1[5] = 60  
#you can append to array
arr1.append(60) 
print arr1  
del arr1[4]
print arr1
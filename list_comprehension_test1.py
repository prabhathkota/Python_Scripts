'''
Created on Sep 12, 2013

@author: 521051
'''

input_arr = [2, 3, 4, 5, 6]   
output_arr = [2*i for i in input_arr if i > 2]   
print("List Comprehnsion Test 1 :", output_arr)    

input_arr = ['Mother Teresa', 'Abraham Lincoln', 'Nelson Mandela']   
output_arr = ['Dear...' + i  for i in input_arr if len(i) > 5]   
print("List Comprehnsion Test 2 :",output_arr)     

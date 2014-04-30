'''
Created on Sep 12, 2013

@author: 521051
'''

import re   
import time   
  
input_str       = "Mother Teresa"  
count_compile   = 0   
count_match     = 0   
  
time_val = time.time()   
  
compiled_regex = re.compile('(\w+)\s+(\w+)')   
  
for i in range(1000000):   
    if compiled_regex.match(input_str):   
        count_compile += 1   
  
print ("Count Compile Value : ", count_compile)           
print("Time taken by Using Compile : ",  time.time() - time_val)   
  
for i in range(1000000):   
    if re.match('(\w+)\s+(\w+)', input_str):   
        count_match += 1   
  
print ("Count Match Value : ", count_compile)             
print("Time taken by Using Match   : ",  time.time() - time_val)    

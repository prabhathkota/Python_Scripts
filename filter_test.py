#filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true   
def isPythonFile(list_1):   
    if list_1.find(".py") == -1:   
        return False   
    else:   
        return True   
    
list_1 = ["1.py","2.pl", "3.zip", "4.py","5.php" ]   
py_files = filter(isPythonFile, list_1)   #Function is called for each element of list   
    
for item in py_files:   
    print("Each item in Filter :" , item)      

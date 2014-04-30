#filter(function, sequence) returns a sequence consisting of those items from the sequence for which function(item) is true
def isPythonFile(list_1):
    if list_1.find(".py") == -1:
        return False
    else:
        return True
 
list_1 = ["1.py","2.pl", "3.zip", "4.py","5.php" ]
py_files = filter(isPythonFile, list_1)   #Function is called for each element of list
 
for item in py_files:
    print("Each item in Filetr :" , item)
    
#O/p:
#1.py
#4.py    
    
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
print("Before Lambda :", list(foo))
print("After  Lambda :", list(filter(lambda x: x % 3 == 0, foo)))

#O/p:
#[18, 9, 24, 12, 27]
    
#map(function, sequence) calls function(item) for each of the sequence's items and returns a list of the return values
print("Before Map :", list(foo))
print("After  Map :", list(map(lambda x: x * 2 + 10, foo)))

#O/P:
#[14, 46, 28, 54, 44, 58, 26, 34, 64]    
    
    
#List comprehension in Python provides a clear and concise syntax for creating lists from other lists    
input_arr = [2, 3, 4]
output_arr = [2*i for i in input_arr if i > 2]
print("List Comprehnsion Test 1 :", output_arr)

#O/P:
#[6, 8]

input_arr = ['Mother Teresa', 'Abraham Lincoln', 'Nelson Mandela']
output_arr = ['Dear...' + i  for i in input_arr if len(i) > 5]
print("List Comprehnsion Test 2 :",output_arr)

#O/P:
#['Dear...Mother Teresa', 'Dear...Abraham Lincoln', 'Dear...Nelson Mandela']



'''
text = 'aaa bbb ccc ddd eee'
filter(lambda x: x != ' ', text)    #Filter object

list(filter(lambda x: x != ' ', text)) # it is capturing in a list

How can I capture filter object in a single variable/scalar
'''
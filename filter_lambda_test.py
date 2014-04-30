foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]   
print("Before Lambda :", list(foo))   
print("After  Lambda :", list(filter(lambda x: x % 3 == 0, foo)))  


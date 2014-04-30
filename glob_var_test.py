def func():
	global x

	print('x is : ', x)    #50
	x = 2
	print('Changed global x to : ', x) #2

x = 50
func()
print ('Value of x is : ', x)  #2
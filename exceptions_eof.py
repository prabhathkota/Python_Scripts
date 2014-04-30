import sys

try:
	s = input('Enter something --> ')
except EOFError:   #(To reproduce EOF, type Ctrl+z)
	print('\nWhy did you do an EOF on me?')
	sys.exit() # exit the program
except:
	print('\nSome error/exception occurred.')
	# here, we are not exiting the program

print('Done')
'''
rstrip() in Python is equivalent to chomp in Perl
lstrip() strips at the front
'''

str = "test string abc \n abc \n aaa\n"

print ("Str : ", str)

print ("Final Str : ", str.rstrip(), end="")
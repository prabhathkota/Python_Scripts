import sys

class nonEmptyValException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, num):
        Exception.__init__(self)
        self.num = num
      
try:
    a = int(input('Enter some integer for Dividend --> '))
    b = int(input('Enter some integer for Divisor --> '))
    
    if not a:
       raise nonEmptyValException(a)
       
    if not b:
       raise nonEmptyValException(b)
    
    c = a/b;    

    print ("Final Value is : ", c) 
    
except  ValueError:
    print('ValueError: Please enter only Integer Value')   
except ZeroDivisionError:
    print('ZeroDivisionError: The input divisor is %d, was expecting a Non-Zero number' % (b))   
except EOFError:
    print('\nWhy did you do an EOF on me?')
except nonEmptyValException as error:
    print('nonEmptyValException: The input is %d, was expecting a integer number' % (error.num))


"""
class ShortLengthException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    s = input('Enter some number --> ')
    if len(s) < 3:
       raise ShortLengthException(len(s), 3)
       #initializing ShortLengthException object
       # Other work can continue as usual here
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortLengthException as error:
    print('ShortLengthException: The input was of length %d, was expecting at least %d' % (error.length, error.atleast))
else:
    print('No exception was raised.')



class HTTPError(Exception):
    # indicates an HTTP protocol error
    def __init__(self, url, errcode, errmsg):
        self.url = url
        self.errcode = errcode
        self.errmsg = errmsg
    def __str__(self):
        return (
            "<HTTPError for %s: %s %s>" %
            (self.url, self.errcode, self.errmsg)
            )

try:
    raise HTTPError("http://www.python.org/foo", 200, "Not Found")
except HTTPError as error:
    print(" url", "=>", error.url)
    print(" errcode", "=>", error.errcode)
    print(" errmsg", "=>", error.errmsg)
    #raise # reraise exception
"""


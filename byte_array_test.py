'''
Created on Sep 13, 2013

@author: 521051
'''

from subprocess import *

#struct pack
#struct unpack

"""
*** bytearray vs array ***
bytearray is the successor of Python 2.x's string type. It's basically the built-in byte array type. Unlike the original string type, it's mutable.
The array module, on the other hand, was created to create binary data structures to communicate with the outside world (for example, to read/write binary file formats).
Unlike bytearray, it supports all kinds of array elements. It's flexible.
So if you just need an array of bytes, bytearray should work fine. If you need flexible formats (say when the element type of the array needs to be determined at runtime), array.array is your friend.
Without looking at the code, my guess would be that bytearray is probably faster since it doesn't have to consider different element types. But it's possible that array('B') returns a bytearray.
"""

""""bytearray vs strings
Unlike strings, bytearray is mutable, i.e., you can change individual bytes "in place" rather than having to create a whole new string
It also makes your intent clear, that you are working with arbitrary bytes rather than text.
"""


import struct
import ctypes

data=ctypes.create_string_buffer(10)
struct.pack_into(">i", data, 5, 0x12345678)
print list(data)

print"\n ----------------------------------------"

from array import array

a = array('B', 'abc')
b = bytearray('abc')

print a
a[0] = 100
b[0] = 'd'

print a
print b

print"\n ----------------------------------------"

hexstrings = ["DE", "AD", "BE", "EF"]   # big-endian 0xDEADBEEF

bytes = bytearray(int(x, 16) for x in hexstrings)
bytes = bytearray.fromhex("".join(hexstrings))     # Python 2.6 may need u""

'''
Once you have defined in __init__.py
You can directly access functions of C &amp; D (which are in the path Package_Sample/sub_folder/)
Main advantage is that you no need to specify the whole path (sub_folder) again and again.
'''

from A import *
from B import *
from sub_folder.C import *
from sub_folder.D import *
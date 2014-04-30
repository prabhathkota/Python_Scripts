'''
Created on Oct 15, 2013

@author: 521051
'''
import subprocess
import sys
theproc = subprocess.Popen("test.py" , shell = True)
theproc.communicate()

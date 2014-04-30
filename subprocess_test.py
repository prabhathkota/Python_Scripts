'''
Created on Sep 13, 2013

@author: 521051
'''
import sys
import subprocess

#theproc = subprocess.Popen([sys.executable, "test.py"])
theproc = subprocess.Popen("array_test.py" , shell = True)
theproc.communicate()

#subprocess.call("dir" , shell = True)

#subprocess.call('date', shell=True)


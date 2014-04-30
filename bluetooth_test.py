'''
Created on Sep 13, 2013

@author: 521051
'''

import bluetooth
import time

nearby_devices = bluetooth.discover_devices()

print "found %d devices" % len(nearby_devices)

for bluetooth_addr in nearby_devices:
    #print bluetooth_addr
    bluetooth_name = bluetooth.lookup_name(bluetooth_addr)
    print bluetooth_name + " ---> " + bluetooth_addr
    
    
#import serial
from serial import *

serialport1 = Serial(port='COM23', baudrate=230400, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=1) 

serialport = Serial(
        port='COM23',
        baudrate=230400,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        timeout=1,
        xonxoff=0,
        rtscts=0,
        interCharTimeout=None
    )

#print serialport.isOpen()

while True:
#     if serialport.inwaiting():
    val = serialport.read(serialport.inwaiting())
    buffer.append(val) # stores all data received into a list
    print(val)  
    print buffer



"""
#open usb-serial device at 250K baud rate
ser = serial.Serial('/dev/ttyUSB0',250000)
# check it gave us the baud rate we wanted
print str(ser.baudrate)

# send an endless stream of "U"s (ascii 0x55, = b01010101)
# out the serial port. Use a frequency counter to check that
# the TX pin is running at baud rate/2
while(True):
    ser.write("U"*256)
"""
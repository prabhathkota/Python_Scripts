from serial import *
from threading import Thread

text_received = ''

def receiveSerialDataFromPort(ser):
    global text_received
    read_buffer = ''

    while True:
        read_buffer += ser.read(ser.inWaiting())
        if '\n' in read_buffer:
            text_received, read_buffer = read_buffer.split('\n')[-2:]
            print text_received

if __name__ ==  '__main__':
    ser = Serial(
        port='COM23',
        baudrate=230400,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        interCharTimeout=None
    )
    
    Thread(target=receiveSerialDataFromPort, args=(ser,)).start()



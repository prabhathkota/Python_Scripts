import time
import sys

try:    
    f = open('read.txt', 'r') 
    while True: # our usual file-reading idiom
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(0.5)  #1/2 sec
        print(line)
except FileNotFoundError:
    print('\n File NOT Found Error')
    sys.exit
except IOError:
    print('\n IO Error')
    sys.exit
except EOFError:
    print('\nWhy did you do an EOF on me?')
    sys.exit
except ValueError:
    print("\nValue Error.")
    sys.exit
finally:
    f.close()
    print('Cleaning up...closed the file')
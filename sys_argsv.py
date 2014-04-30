import sys
import os

def readfile(filename):
    '''Print a file to the standard output.'''
    
    #if not os.path.exists(filename):     #if file not present
    #    print("\n File not present")
        #sys.exit()
        
    try:   #Exceptions      
        f = open(filename, 'r')
        while True: 
            line = f.readline()
            if len(line) == 0:
                break
            print(line,) # notice comma
        f.close()
    except FileNotFoundError:
        print("\n File not found")
    
# Script starts from here
if len(sys.argv) < 2:
    print('No action specified.')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        #Format inside print statement
        print('''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
  --version : Prints the version number
  --help    : Display this help''')
    else:
        print('Unknown option.')
    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)
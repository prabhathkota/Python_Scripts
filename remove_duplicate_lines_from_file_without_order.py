#When we use sets concept, the order is not same (order is not considered)

try:
    input_file = open("file_with_duplicates.txt", "r")
    output_file = open("file_without_duplicates.txt","w")

    #The main drawback of using sets is, the order of the lines may not be same as in the input file
    uniquelines = set(input_file.read().split("\n"))
    output_file.write("".join([line + "\n" for line in uniquelines]))
    
    input_file.close()
    output_file.close()
    
except FileNotFoundError:
    print('\n File NOT Found Error')
    sys.exit
except IOError:
    print('\n IO Error')
    sys.exit    
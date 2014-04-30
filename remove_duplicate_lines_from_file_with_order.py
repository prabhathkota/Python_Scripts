#We didn't use sets concept because sets does not consider order

try:
    input_file = open("file_with_duplicates.txt", "r")
    output_file = open("file_without_duplicates.txt", "w")

    unique = []
    for line in input_file:
        line = line.strip()
        if line not in unique:
            unique.append(line)
    input_file.close()
    
    for i in range(0, len(unique)-1):
        unique[i] += "\n"

    output_file.writelines(unique)
    output_file.close
    
except FileNotFoundError:
    print('\n File NOT Found Error')
    sys.exit
except IOError:
    print('\n IO Error')
    sys.exit
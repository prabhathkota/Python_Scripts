#!C:\Python33\python.exe -u

file = open("read.txt","r")
text = file.readlines()
file.close()

text.reverse()

for line in text:
    print(line)

#!C:\Python33\python.exe -u

file = open("read.txt","r")
text = file.readlines()		#Read all lines from read.txt
file.close()

file2 = open ("write.txt", "w")		
#Write all lines from read.txt into write.txt
#It overrides if any content already present in write.txt
file2.writelines(text)
file2.close

file2 = open ("append.txt", "a")
#It appends content from read.txt into append.txt
file2.writelines(text)
file2.close


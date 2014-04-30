students = ["Mahatma Gandhi", "Mother Teresa", "Paul Coelho", "Bill Gates", "Steve Jobs"]

new_students = students[:]

for student in new_students:
     print("Do you want to keep student", student, "?")
	 #print "Do you want to keep student", student, "?"
     answer = input("yes/no ")
	 #answer = raw_input ("yes/no ")
     if answer != "yes":
         students.remove(student)
		 
print(students)
#print students


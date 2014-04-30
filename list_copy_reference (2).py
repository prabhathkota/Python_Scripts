inspiring_ppl = ["Mahatma Gandhi", "Mother Teresa", "Paul Coelho", "Bill Gates", "Steve Jobs"]

#The following Shares same memory location
inspiring_ppl_1 = inspiring_ppl

inspiring_ppl.append("Abdul Kalam")
inspiring_ppl_1.append("Abraham Lincoln")

#Therefore inspiring_ppl, inspiring_ppl_1 contains the same contents including "Abdul Kalam" and "Abraham Lincoln"

#Python does not have variables like C 
#In Python variables are just tags attached to objects

#The following shares different memory location
inspiring_ppl_2 = inspiring_ppl[:]

inspiring_ppl.append("Swami Vivekananda")

print(inspiring_ppl)

print(inspiring_ppl_1)

print(inspiring_ppl_2)
 
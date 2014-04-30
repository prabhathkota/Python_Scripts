import Employee1
#from Employee1 import Employee1

e1 = Employee1.Employee1("Sarah111",99999,30000)

print("Employee1 Details 111:")
print(" Name:", e1.name, "Code:", e1.empCode, "Pay:", e1.pay)

e1.get_value(789)

"""
class Employee1:

   def __init__(self, name, empCode,pay):
      self.name=name
      self.empCode=empCode
      self.pay=pay

e1 = Employee1("Sarah",99,30000.00)
e2 = Employee1("Asrar",100,60000.00)

print("Employee1 Details:")
print(" Name:", e1.name, "Code:", e1.empCode, "Pay:", e1.pay)
print(" Name:", e2.name, "Code:", e2.empCode, "Pay:", e2.pay)
"""


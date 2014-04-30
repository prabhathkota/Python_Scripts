class Parent:        # define parent class
   parentAmount = 100
   def __init__(self):
      print("Calling parent constructor")

   def parentFunc(self):
      print('Calling parent function')

   def setAmount(self, amount):
      Parent.parentAmount = amount

   def getAmount(self):
      print("Parent attribute :", Parent.parentAmount)

class Child(Parent): # define child class
   def __init__(self):
      print("Calling child constructor")

   def childFunc(self):
      print('Calling child function')

c = Child()          # instance of child
c.childFunc()        # child calls its function
c.parentFunc()       # calls parent's function
c.setAmount(200)     # again call parent's function
c.getAmount()        # again call parent's function
### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
ageofqueen = 78

# define some functions
def printhello():
    #print("hello")
    return "Hello"
    
def timesfour(input):
    #print("Mutiplied Value : " , input * 4)
    return (input*4)
    
# define a class
class Piano:
    def __init__(self, type, height, price, age):
        #self.type = input("What type of piano? ")
        #self.height = input("What height (in feet)? ")
        #self.price = input("How much did it cost? ")
        #self.age = input("How old is it (in years)? ")
        self.type = type
        self.height = height
        self.price = price
        self.age = age
        

    def printdetails(self):
        print("This piano Height is :" + self.height + " foot ")
        print("This piano Type is :" + self.type + " type ")
        print("This piano Price is :" , str(self.price) + " dollars ")
        print("This piano Age is :" , str(self.age) + " years")
        
		#print(self.type + "piano " + self.age + " years old and costing :" + self.price + " dollars")
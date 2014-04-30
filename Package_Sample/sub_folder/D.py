### EXAMPLE PYTHON MODULE
# Define some variables:
    

class D:
    def __init__(self, type, height, price, age):
        self.type = type
        self.height = height
        self.price = price
        self.age = age
        
    def print_details(self):
        print("\nThis D Type is  :" + self.type + " type ")
        print("This D Height is  :" + self.height + " foot ")
        print("This D Price is   :" , str(self.price) + " dollars ")
        print("This D Age is     :" , str(self.age) + " years")
        
        

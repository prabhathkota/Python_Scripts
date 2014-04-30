### EXAMPLE PYTHON MODULE

class B:
    def __init__(self, type, height, price, age):
        self.type = type
        self.height = height
        self.price = price
        self.age = age
        
    def print_details(self):
        print("\nThis B Type is    :" + self.type + " type ")
        print("This B Height is    :" + self.height + " foot ")
        print("This B Price is     :" , str(self.price) + " dollars ")
        print("This B Age is       :" , str(self.age) + " years")
        
        
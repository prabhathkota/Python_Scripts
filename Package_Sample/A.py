### EXAMPLE PYTHON MODULE

class A:
    def __init__(self, type, height, price, age):
        self.type = type
        self.height = height
        self.price = price
        self.age = age
        
    def print_details(self):
        print("\nThis A Type is  :" + self.type + " type ")
        print("This A Height is  :" + self.height + " foot ")
        print("This A Price is   :" , str(self.price) + " dollars ")
        print("This A Age is     :" , str(self.age) + " years")

        
        
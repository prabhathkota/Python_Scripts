### EXAMPLE PYTHON MODULE

   
class C:
    def __init__(self, type, height, price, age):
        self.type = type
        self.height = height
        self.price = price
        self.age = age
        
    def print_details(self):
        print("\nThis C Type is  :" + self.type + " type ")
        print("This C Height is  :" + self.height + " foot ")
        print("This C Price is   :" , str(self.price) + " dollars ")
        print("This C Age is     :" , str(self.age) + " years")

        
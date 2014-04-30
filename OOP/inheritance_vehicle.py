class Vehicle:
    '''Represents any Vehicle.'''
    def __init__(self, name, model):
        self.name = name
        self.model = model
        print('Initialized Vehicle: %s' % self.name)
    
    def details(self):
        '''Call my details.'''
        print('Name:"%s" model:"%s"' % (self.name, self.model))

class Car(Vehicle):
    '''Represents a Car.'''
    def __init__(self, name, model, price):
        Vehicle.__init__(self, name, model)
        self.price = price
        print('Initialized Car: %s' % self.name)

    def details(self):
        Vehicle.details(self)
        print('price: "%d"' % self.price)

class Truck(Vehicle):
    '''Represents a Truck.'''
    def __init__(self, name, model, price):
        Vehicle.__init__(self, name, model)
        self.price = price
        print('Initialized Truck: %s' % self.name)
    
    def details(self):
        Vehicle.details(self)
        print('price: "%d"' % self.price)

c = Car('Cooper', 100, 30000)
t = Truck('Jeep', 200, 50000)

print() # prints a blank line

vehicles = [c, t]
for member in vehicles:
    print() # prints a blank line
    member.details() # works for both Cars and Trucks
                
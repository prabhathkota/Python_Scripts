class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    description = "This shape has not been described yet"
    author = "Nobody has claimed to make this shape yet"
    def area(self):
        return self.x * self.y
    
    def perimeter(self):
        return 2 * self.x + 2 * self.y
    
    def describe(self,text):
        if (text):
            self.description = text
            
        return self.description
    
    def authorName(self,text):
        if (text):
            self.author = text
            
        return self.author        
    
    def scaleSize(self,scale):
        self.x = self.x * scale
        self.y = self.y * scale
    
class Square(Shape):
    def __init__(self,x):
        self.x = x
        self.y = x

     
sq_obj = Square(10) #Through Inheritance
print("Area of Square : ", sq_obj.area())

rect_obj = Shape(10,20) #Calling Shape directly
print("Area of Rectangle : ", rect_obj.area())
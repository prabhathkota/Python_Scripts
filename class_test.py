class Shape:

    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    description = "This shape has not been described yet"   #Default Value
    author = "Nobody has claimed to make this shape yet"    #Default Value
    
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
    

rectangle = Shape(10,20)

#finding the area of your rectangle:
print("Area :", rectangle.area())

#finding the perimeter of your rectangle:
print("Perimeter : ", rectangle.perimeter())

#describing the rectangle
print(rectangle.describe("A wide rectangle, more than twice as wide as it is tall"))
print(rectangle.authorName(""))

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)

#re-printing the new area of the rectangle
print("Area after Scaling : ", rectangle.area())
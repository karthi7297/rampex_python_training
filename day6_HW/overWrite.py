class Shape:
    def area(self):
        print("Area of shape")
class Rectangle(Shape):
    def area(self,length,breadth):
        print(length*breadth)
class Circle(Shape):
    def area(self,radius):
        print(3.14*radius*radius)
c=Circle()
c.area(5)
b=Rectangle()
b.area(5,6)
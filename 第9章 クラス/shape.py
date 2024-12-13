class Shape():

    def __init__(self, name):
        self.name = name
        
    def area(self):
        print("面積を計算できません")

class Rectangle(Shape):

    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        rectangle_area = self.width * self.height
        print(rectangle_area)

class Circle(Shape):

    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        circle_area = 3.14 * self.radius**2
        print(circle_area)

class Square(Rectangle):

    def __init__(self, name, side):
        super().__init__(name, side, side)
        self.side = side

    def area(self):
        return super().area()
    
rectangle1 = Rectangle('長方形', 15, 4)
rectangle1.area()

circle1 = Circle('円', 3)
circle1.area()

square1 = Square('正方形', 6)
square1.area()


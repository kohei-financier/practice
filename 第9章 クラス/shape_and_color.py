class Shape():

    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def area(self):
        print("面積を計算できません")

class Drawable():

    def __init__(self):
        pass

    def draw(self):
        print("図形を描画します")

class Rectangle(Shape, Drawable):

    def __init__(self, name, color, width, height):
        super().__init__(name, color)
        self.width = width
        self.height = height

    def area(self):
        rectangle = self.width * self.height
        return rectangle
    
    def draw(self):
        print(f"{self.color}色の長方形を描画します")

class Circle(Shape, Drawable):

    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        circle = self.radius**2 * 3.14
        return circle
    
    def draw(self):
        print(f"{self.color}色の円を描画します")
    
class Triangle(Shape, Drawable):

    def __init__(self, name, color, base, height):
        super().__init__(name, color)
        self.base = base
        self.height = height

    def area(self):
        triangle = self.base * self.height / 2
        return triangle
    
    def draw(self):
        print(f"{self.color}色の三角形を描画します")

rectangle1 = Rectangle('長方形', 'red', 10, 5)
print(f"{rectangle1.name} の面積: {rectangle1.area()}")
rectangle1.draw()

circle1 = Circle('円', 'yellow', 5)
print(f"{circle1.name} の面積: {circle1.area()}")
circle1.draw()

triangle = Triangle('三角形', 'blue', 10, 4)
print(f"{triangle.name} の面積: {triangle.area()}")
triangle.draw()
from Figure import Figure

#Класс прямоугольник
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length  # Атрибут с длиной
        self.width = width  # Атрибут с шириной
        self.corners = 4

    name = "Rectangle"
    corners = 4

    @property
    def area(self):
        return self.length * self.width

    @property
    def perimeter(self):
        return self.length * 2 + self.width * 2



from Figure import Figure


## Класс квадрат
class Square(Figure):
    def __init__(self, side):
        self.side = side

    name = "Square"
    corners = 4

    @property
    def area(self):
        return self.side * self.side  # Получаем площадь квадрата

    @property
    def perimeter(self):
        return self.side * 4

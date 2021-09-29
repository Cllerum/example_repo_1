from Figure import Figure

##Класс круг
class Circle(Figure):
    def __init__(self, diameter):
        self.diameter = diameter

    name = "Circle"
    corners = 0

    @property
    def radius(self):
        return self.diameter*2 #Получаем диаметр круга

    @property
    def area(self):
        return 3.14*self.radius**2 #Получаем площадь круга
    @property
    def perimeter(self):
        return 3.14*self.radius*2 #Получаем периметр круга

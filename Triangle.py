from Figure import Figure

##Класс Треугольник

class Triangle(Figure):
    def __init__(self, sideA, sideB, sideC):
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC
    name = "Triangle"
    corners = 3

    @property
    def perimeter(self):
        return self.sideA+self.sideB+self.sideC #Получаем периметр

    @property
    def area(self):
       self.halfPerimeter = self.perimeter/2
       return (self.halfPerimeter*(self.halfPerimeter - self.sideA)*(self.halfPerimeter - self.sideB)*(self.halfPerimeter - self.sideC))**0.5 #Получаем площадь по формуле герона


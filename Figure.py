class Figure:
    def __init__(self, name, corners):  # Объявил обязательные свойства
        self.corners = corners  # Атрибут с количеством углов
        self.name = name  # Атрибут с именем
    def add_area(self, figure):
        return self.area + figure.area



from Figure import Figure
from Square import Square
from Triangle import Triangle
from Rectangle import Rectangle
from Circle import Circle


figureInstance1 = Figure(name="Фигура", corners=3)
сircleInstance1 = Circle(2)
rectangleInstance1 = Rectangle(1, 1)  # Достаточно указать значения, без указания свойств
squareInstance1 = Square(5)
triangleInstance1 = Triangle(1, 1, 1)

print(figureInstance1.corners)
print(triangleInstance1.add_area(сircleInstance1))
print(triangleInstance1.area)
print(сircleInstance1.area)
print(squareInstance1.perimeter)
print(rectangleInstance1.perimeter)

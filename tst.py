class Car:
    def __init__(self, brand, type_body):  # Объявил обязательные свойства
        self.brand = brand,
        self.type_body = type_body

    wheel = 4

    def start_engine(self):  # Создал функцию
        print(f"Запущен двигатель {self.brand} {self.type_body}")


# Создали класс


class Saer:
    pass


print(Car)


class Bugatti(Car):  # Создали подкласс
    hp = 1001  # Объявили атрибуты
    speed = 400
    brand = 'Bugatti',  # Объявляю атрибуты у нового экземпляра класса
    type_body = 'gipercar'

    def zapusk():
        print("РАТАТАТАТА")


a = Bugatti(
    brand='Bugatti',  # Объявляю атрибуты у нового экземпляра класса
    type_body='gipercar'
)

if isinstance(a, Saer):
    print("Да, это Car.")
else:
    print("Нет, это другое.")

print(issubclass(Car, Bugatti))

print(Bugatti.hp)
print(id(Bugatti))  # Обращаемся к ID обьекта

Honda = Car(
    brand='honda',  # Объявляю атрибуты у нового экземпляра класса
    type_body='sportcoupe'
)
Honda.start_engine()
Bugatti.zapusk()


# isinstance(а,б) - метод позволяет выяснить является ли а инстансом класса б
# issubclass(а,б) - метод позволяет выяснить является ли а подкласом по отношению к б


class Animal:
    sound = None

    def produce_sound(self):
        print({self.sound})


class Dog(Animal):
    pass

class Cat(Animal):
    sound = "Meow"

cat = Cat()
dog = Dog()

dog.produce_sound()
cat.produce_sound()
#@property - декоратор превращающий значение функции на выходе в атрибут
#@staticmethod - декоратор отключающий необходимость в передаче функции переменных

#__str__ - метод задает поведение для объекта при выводе как строку __repr__ - подобный метод, в случае когда перечисляем в массиве
#__add__ - задает поведение при сложении
#__call__ - можно вызвать как функцию (методом collable можно проверить является ли объект вызываемым)
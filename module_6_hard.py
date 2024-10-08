
import math

class Figure:
    sides_count = 0
    def __init__(self, color=(0, 0, 0), sides=None):
        self.__color = color
        self.__sides = sides if sides is not None else []
        self.filled = True

    def __is_valid_color(self, r, g, b):
        return all((0 <= r <= 255, 0 <= g <= 255, 0 <= b <=255))

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            return f'Некорректные значения цвета'
        else:
            self.__color = (r, g, b)

    def get_color(self):
        return list(self.__color)

    def __is_valid_sides(self, *sides):
        return isinstance(sides[0], int) and sides[0] > 0

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, color=(0, 0, 0), radius=1):
        super().__init__(color=color)
        self.radius = radius

    def get_square(self):
        return math.pi*self.radius**2


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color=(0, 0, 0), a=1, b=1, c=1):
        super().__init__(color=color)
        self.set_sides(a, b, c)

    def get_square(self):
        s = sum(self.get_sides()) / 2
        a, b, c = self.get_sides()
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color=(0, 0, 0), side_length=1):
        super().__init__(color=color)
        self.set_sides(*[side_length] * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
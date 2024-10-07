class Figure:
    sides_count = 0
    def __init__(self, __sides, __color=(0, 0, 0), filled=True):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = int(__sides)

    def __is_valid_color(self, r, g, b):
        return all((0 <= r <= 255, 0 <= g <= 255, 0 <= b <=255))

    def set_color(self, r, g, b):
        if not self.__is_valid_color(r, g, b):
            raise ValueError('Некорректные значения цвета')
        else:
            self.__color = (r, g, b)

    def get_color(self, r, g, b):
        RGB_colors = []
        if self.__is_valid_color(r, g, b):
            RGB_colors.append(self.__color)

    def __is_valid_sides(self, *sides):
        if isinstance(sides, int) and sides > 0:
            return True
        else:
            return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return self.__sides.sum()

    def set_sides(self, *new_sides):
        if int(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1
    def __init__(self, __sides, __color=(0, 0, 0)):
        super().__init__( __sides, (0, 0, 0), filled=True)
        self.radius = __sides/6.28

    def get_square(self):
        return 3.14*self.radius**2



circle1 = Circle(10,(200, 200, 100)) # (Цвет, стороны)
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
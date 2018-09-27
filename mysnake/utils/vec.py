

class Vec:

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, arg: int):
        return Vec(self.x * arg, self.y * arg)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)


UP = Vec(0, -1)
RIGHT = Vec(1, 0)
DOWN = Vec(0, 1)
LEFT = Vec(-1, 0)
DIR_VECTORS = [UP, RIGHT, DOWN, LEFT]
NULL_VEC = Vec(0, 0)
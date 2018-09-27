from mysnake.utils.vec import *
from pygame import Surface
from random import randint


FIELD_COLORS = [(51, 102, 0), (56, 112, 0), (71, 142, 0), (76, 152, 0)]


class Field:

    def __init__(self, size: int):
        self.size = size
        self.things = set()
        self.build_walls()

    def element_at(self, loc: Vec):
        for e in self.things:
            if e.loc == loc:
                return e
        return None

    def is_free(self, loc: Vec) -> bool:
        return self.element_at(loc) is None

    def add(self, thing):
        thing.loc = self.get_coord(thing.loc)
        self.things.add(thing)

    def get_random_location(self) -> Vec:
        v = Vec(randint(0, self.size - 1), randint(0, self.size - 1))
        while not self.is_free(v):
            v = Vec(randint(0, self.size - 1), randint(0, self.size - 1))
        return v

    def draw(self, screen: Surface):
        screen.fill(FIELD_COLORS[0])
        s = screen.get_height() // self.size
        for thing in self.things:
            thing.draw(screen, thing.loc.x * s, thing.loc.y * s, s)

    def get_coord(self, v: Vec) -> Vec:
        return Vec(v.x % self.size, v.y % self.size)

    def get_dir_vec(self, v_from: Vec, v_to: Vec) -> Vec:
        dv = v_to - v_from
        if dv.x < -1:
            dv.x = 1
        elif dv.x > 1:
            dv.x = -1
        elif dv.y < -1:
            dv.y = 1
        elif dv.y > 1:
            dv.y = -1
        return dv

    def clear(self):
        self.things.clear()
        self.build_walls()

    # abstract
    def build_walls(self):
        pass

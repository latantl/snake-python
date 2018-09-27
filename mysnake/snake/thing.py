from mysnake.snake.field import *
from mysnake.utils.event import Event
import pygame.gfxdraw


class ThingCreatingException(Exception):
    pass


class Thing:

    def __init__(self, field: Field, location: Vec):
        self.field: Field = field
        self.loc: Vec = location
        field.add(self)
        self.died = Event()
        self.id = Thing.id_count
        Thing.id_count = Thing.id_count + 1

    def set_location(self, loc: Vec):
        self.loc = self.field.get_coord(loc)

    def remove_from_field(self):
        self.field.things.remove(self)

    # abstract
    def collide(self, head):
        pass

    # abstract
    def die(self) -> None:
        self.died.fire(self)

    def draw_circle(self, screen, x, y, size, color):
        pygame.gfxdraw.aacircle(screen, x + size // 2, y + size // 2, size // 2 - 1, color)
        pygame.gfxdraw.filled_circle(screen, x + size // 2, y + size // 2, size // 2 - 1, color)

    # abstract
    def draw(self, screen, x: int, y: int, size: int):
        pass


Thing.id_count = 0
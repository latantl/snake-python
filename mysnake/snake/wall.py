from mysnake.snake.thing import *
from pygame import draw


WALL_COLOR = (102, 51, 0)


class Wall(Thing):

    def __init__(self, field: Field, loc: Vec, color: (int, int, int) = WALL_COLOR):
        super(Wall, self).__init__(field, loc)
        self.color = color

    def collide(self, head):
        head.die()
    
    def die(self):
        super(Wall, self).die()
        self.remove_from_field()

    def draw(self, screen, x: int, y: int, size: int):
        draw.rect(screen, self.color, (x, y, size, size))
        draw.rect(screen, (0, 0, 0), (x, y, size, size), 1)
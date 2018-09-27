from mysnake.snake.thing import *
from pygame import draw


class Segment(Thing):

    def __init__(self, field: Field, loc: Vec, color: (int, int, int)):
        super(Segment, self).__init__(field, loc)
        self.color = color

    # abstract
    def swap_neighbour(self, new, old=None):
        """
        Call from current neighbour.
        :type new: Segment
        :type old: Segment
        """

    def step_to(self, sender):
        """
        :type sender: Segment
        """
        self.set_location(sender.loc)

    def draw_neighbour_connection(self, screen, neighbour, x: int, y: int, size: int):
        dv = self.field.get_dir_vec(neighbour.loc, self.loc)
        rect = None
        if dv == UP:
            rect = (x + 1, y + size // 2 + 1, size - 2, size // 2 )
        elif dv == DOWN:
            rect = (x + 1, y, size - 2, size // 2)
        elif dv == RIGHT:
            rect = (x, y + 1, size // 2, size - 2)
        elif dv == LEFT:
            rect = (x + size // 2 + 1, y + 1, size // 2, size - 2 )
        draw.rect(screen, self.color, rect, 0)
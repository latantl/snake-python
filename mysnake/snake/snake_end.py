from mysnake.snake.snake_segment import *


class End(Segment):

    def __init__(self, field: Field, loc: Vec = NULL_VEC, color = (int, int, int)):
        super(End, self).__init__(field, loc, color )
        self.neighbour: Segment = None

    def __str__(self):
        return super(End, self).__str__() + f' {self.neighbour.id} end'

    def swap_neighbour(self, new: Segment, old: Segment = None) -> None:
        self.neighbour = new

    def collide(self, head):
        head.die()

    def draw(self, screen: Surface, x: int, y: int, size: int):
        self.draw_circle(screen, x, y, size, self.color)
        self.draw_neighbour_connection(screen, self.neighbour, x, y, size)
from mysnake.snake.snake_segment import *


# Head creates the Body segments
class Body(Segment):

    def __init__(self, field: Field, parent, color: (int, int, int)):
        super(Body, self).__init__(field, parent.loc, color)
        parent.neighbour.swap_neighbour(old=parent, new=self)
        self.neighbour1: Segment = parent.neighbour
        self.neighbour2: Segment = parent

        parent.swap_neighbour(self)

    def step_to(self, sender: Segment):
        if sender == self.neighbour1:
            self.neighbour2.step_to(self)
        elif sender == self.neighbour2:
            self.neighbour1.step_to(self)
        super(Body, self).step_to(sender)

    def swap_neighbour(self, old, new: Segment = None):
        if old == self.neighbour1:
            self.neighbour1 = new
        elif old == self.neighbour2:
            self.neighbour2 = new

    def collide(self, head):
        head.die()

    def draw(self, screen, x: int, y: int, size: int):
        self.draw_circle(screen, x, y, size, self.color)
        self.draw_neighbour_connection(screen, self.neighbour1, x, y, size)
        self.draw_neighbour_connection(screen, self.neighbour2, x, y, size)

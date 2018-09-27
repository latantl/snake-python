from mysnake.snake.snake_end import *
from mysnake.snake.snake_body import Body
from mysnake.snake.fruit import Fruit


# abstract
class Head(End):

    def __init__(self, field: Field, loc: Vec, dir_vec: Vec, color: (int, int, int), body_color: (int, int, int)):
        super(Head, self).__init__(field, loc, color)
        self.eat_event = Event()
        self.dir_vec = dir_vec
        self.body_color = body_color

    def update_dir_vec(self) -> Vec:
        self.dir_vec = self.loc - self.neighbour.loc
        return self.dir_vec

    def step(self, direction: Vec):
        if not self.dir_vec + direction == NULL_VEC:
            self.dir_vec = direction
        destination = self.field.get_coord(self.loc + self.dir_vec)
        element_at_destination = self.field.element_at(destination)
        if element_at_destination is None:
            self.neighbour.step_to(self)
            self.set_location(destination)
        else:
            element_at_destination.collide(self)

    def extend_in_direction(self, dir_vec: Vec):
        Body(self.field, self, self.body_color)
        self.set_location(self.loc + dir_vec)
        self.dir_vec = dir_vec

    def eat(self, fruit: Fruit):
        self.eat_event .fire(fruit)
        Body(self.field, self, self.body_color)
        self.set_location(fruit.loc)

    def collide(self, sender):
        pass

    def die(self, event=None):
        super(Head, self).die()

    def draw(self, screen, x: int, y: int, size: int):
        self.draw_circle(screen, x, y, size, self.color)
        self.draw_neighbour_connection(screen, self.neighbour, x, y, size)
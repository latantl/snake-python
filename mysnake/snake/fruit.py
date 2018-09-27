from mysnake.snake.thing import *


FRUIT_COLORS = [(178,255,102), (255,51,51), (255,255,0), (255,128,0)]


class Fruit(Thing):

    def __init__(self, field: Field, can_reborn: bool = True, color: (int, int, int) = None):
        super(Fruit, self).__init__(field, field.get_random_location())
        self.can_reborn = can_reborn
        if color is None:
            self.color = FRUIT_COLORS[randint(0, len(FRUIT_COLORS) - 1)]
        else:
            self.color = color

    def collide(self, head) -> None:
        head.eat(self)
        self.die()

    def die(self) -> None:
        self.remove_from_field()
        if self.can_reborn:
            self.loc = self.field.get_random_location()
            self.field.add(self)
        super(Fruit, self).die()

    def draw(self, screen, x: int, y: int, size: int):
        self.draw_circle(screen, x, y, size, self.color)
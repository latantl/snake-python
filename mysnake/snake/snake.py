from mysnake.snake.snake_head import *


SNAKE_BODY_COLORS = [(0, 128, 255), (255, 255, 0)]
SNAKE_HEAD_COLORS = [(102, 178, 255), (255, 255, 153)]


# abstract
class Snake:

    def __init__(self, start_dir: Vec):
        self.is_alive = True
        self.point = 0
        self.step_dir_vec = start_dir
        self.head = None

    def set_direction(self, dir_vec: Vec):
        self.step_dir_vec = dir_vec

    def func_when_died(self, event=None):
        self.is_alive = False

    def func_wen_eating(self, event=None):
        self.point = self.point + 1

    def step(self):
        self.head.step(self.step_dir_vec)

    def turn_right(self):
        self.step_dir_vec = DIR_VECTORS[(DIR_VECTORS.index(self.step_dir_vec) + 1) % len(DIR_VECTORS)]

    def turn_left(self):
        self.step_dir_vec = DIR_VECTORS[(DIR_VECTORS.index(self.step_dir_vec) - 1) % len(DIR_VECTORS)]


class OneHeadedSnake(Snake):

    def __init__(self, field: Field, loc: Vec, dir_vec: Vec, body_color: (int, int, int), head_color: (int, int, int)):
        super(OneHeadedSnake, self).__init__(dir_vec)
        self.head = Head(field, loc, dir_vec, head_color, body_color)
        self.tail = End(field, loc - dir_vec, body_color)
        self.head.neighbour = self.tail
        self.tail.neighbour = self.head
        self.head.died.sub(self.func_when_died)
        self.head.eat_event.sub(self.func_wen_eating)


class TwoHeadedSnake(Snake):

    def __init__(self, field: Field, loc: Vec, dir_vec: Vec, body_color: (int, int, int), head_color: (int, int, int)):
        super(TwoHeadedSnake, self).__init__(dir_vec)
        self.head1 = Head(field, loc, dir_vec, head_color, body_color)
        self.head2 = Head(field, loc - dir_vec, NULL_VEC - dir_vec, head_color, body_color)
        self.head1.neighbour = self.head2
        self.head2.neighbour = self.head1
        self.head1.died.sub(self.func_when_died)
        self.head2.died.sub(self.func_when_died)
        self.head1.eat_event.sub(self.func_wen_eating)
        self.head2.eat_event.sub(self.func_wen_eating)
        self.head = self.head1

    def switch_head(self):
        if self.head == self.head1:
            self.head = self.head2
        else:
            self.head = self.head1
        self.step_dir_vec = self.head.update_dir_vec()
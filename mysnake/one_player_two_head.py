from mysnake.snakestate import *


class OnePlayerTwoHead(SnakeState):

    def __init__(self, field: Field):
        super(OnePlayerTwoHead, self).__init__(field, 100)
        half = field.size // 2
        self.snake = TwoHeadedSnake(field, Vec(half, half), UP, SNAKE_BODY_COLORS[0], SNAKE_HEAD_COLORS[0])
        for i in range(10):
            Fruit(field)

    def input(self, event: pygame_event):
        if not self.is_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake.turn_left()
            if event.key == pygame.K_RIGHT:
                self.snake.turn_right()
            if event.key == pygame.K_DOWN:
                self.snake.switch_head()
        super(OnePlayerTwoHead, self).input(event)

    def snake_step(self):
        self.snake.step()

    def draw(self, screen: Surface):
        super(OnePlayerTwoHead, self).draw(screen)
        self.draw_string(screen, self.snake.point.__str__(), self.point_font, self.snake.head.color, 3, 0)

    def is_game_over(self):
        return not self.snake.is_alive

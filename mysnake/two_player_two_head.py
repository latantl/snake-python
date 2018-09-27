from mysnake.snakestate import *


class TwoPlayerTwoHead(SnakeState):

    def __init__(self, field: Field):
        super(TwoPlayerTwoHead, self).__init__(field, 100)
        half = field.size // 2
        self.snake1 = TwoHeadedSnake(field, Vec(half - 2, half - 1), UP, SNAKE_BODY_COLORS[0], SNAKE_HEAD_COLORS[0])
        self.snake1.head.extend_in_direction(RIGHT)
        self.snake1.head.extend_in_direction(RIGHT)
        self.snake1.head.extend_in_direction(UP)
        self.snake1.head.extend_in_direction(LEFT)
        self.snake2 = TwoHeadedSnake(field, Vec(half + 1, half), DOWN, SNAKE_BODY_COLORS[1], SNAKE_HEAD_COLORS[1])
        self.snake2.head.extend_in_direction(LEFT)
        self.snake2.head.extend_in_direction(LEFT)
        self.snake2.head.extend_in_direction(DOWN)
        self.snake2.head.extend_in_direction(RIGHT)
        for i in range(10):
            Fruit(field)

    def input(self, event: pygame_event):
        if not self.is_over and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.snake2.turn_left()
            if event.key == pygame.K_RIGHT:
                self.snake2.turn_right()
            if event.key == pygame.K_DOWN:
                self.snake2.switch_head()
            if event.key == pygame.K_a:
                self.snake1.turn_left()
            if event.key == pygame.K_d:
                self.snake1.turn_right()
            if event.key == pygame.K_s:
                self.snake1.switch_head()
        super(TwoPlayerTwoHead, self).input(event)

    def snake_step(self):
        self.snake1.step()
        self.snake2.step()

    def draw(self, screen: Surface):
        super(TwoPlayerTwoHead, self).draw(screen)
        self.draw_string(screen, self.snake1.point.__str__(), self.point_font, self.snake1.head.color, 3, 0)
        self.draw_string(screen, self.snake2.point.__str__(), self.point_font, self.snake2.head.color, 3, 20)

    def is_game_over(self):
        if not self.snake1.is_alive:
            self.snake1.point = 0
            return True
        if not self.snake2.is_alive:
            self.snake2.point = 0
            return True
        return False
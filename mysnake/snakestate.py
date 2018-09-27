from mysnake.utils.state import *
from mysnake.snake.snake import *


class SnakeState(State):

    def __init__(self, field: Field, delay: int):
        super(SnakeState, self).__init__()
        self.is_started = False
        self.is_over: bool = False
        self.is_paused: bool = False
        self.field: Field = field
        self.delay = delay
        self.info_font = pygame.font.SysFont("arial", 50)
        self.point_font = pygame.font.SysFont("arial", 20)

    def reset_timer(self):
        self.start = pygame.time.get_ticks()
        self.stepped = 0

    def input(self, event: pygame_event):
        if event.type == pygame.KEYDOWN:
            if (self.is_paused or self.is_over or not self.is_started) and event.key == pygame.K_ESCAPE:
                self.field.clear()
                self.manager.go_back()
            if not self. is_over and event.key == pygame.K_RETURN:
                if not self.is_started:
                    self.is_started = True
                    self.reset_timer()
                    return
                self.reset_timer()
                self.is_paused = not self.is_paused

    def draw(self, screen: Surface):
        self.field.draw(screen)
        string = ""
        if not self.is_started:
           string = "Press ENTER to start!"
        elif self.is_paused:
            string = "Game Paused"
        elif self.is_over:
            string = "Game Over"
        else:
            return
        str_width, str_height = self.info_font.size(string)
        self.draw_string(screen, string, self.info_font, (255, 255, 255),
                         (screen.get_width() - str_width)// 2, int(screen.get_height() * 0.3))

    def draw_string(self, screen: Surface, string, font, color, x: int, y: int):
        label = font.render(string, 1, color)
        screen.blit(label, (x, y))

    def on_run(self):
        if self.is_started and not self.is_over and not self.is_paused:
            if (pygame.time.get_ticks() - self.start) // self.delay > self.stepped:
                self.stepped = self.stepped + 1
                self.step()

    def step(self):
        self.snake_step()
        self.is_over = self.is_game_over()

    # abstract
    def is_game_over(self):
        pass

    # abstract
    def snake_step(self):
        pass
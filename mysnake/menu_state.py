from pygame import KEYDOWN, K_UP, K_DOWN, K_RETURN, font
from mysnake.utils.state import *
from mysnake.snake.walled_field import WalledField
from mysnake.two_player_one_head import TwoPlayerOneHead
from mysnake.two_player_two_head import TwoPlayerTwoHead
from mysnake.one_player_one_head import OnePlayerOneHead
from mysnake.one_player_two_head import OnePlayerTwoHead

class MenuState(State):

    def __init__(self):
        self.items = ["One Player, One Head", "One Player, Two Head",
                        "Two Player, One Head", "Two Player, Two Head"]
        self.index = 0
        self.field = WalledField(60)
        self.item_font = font.SysFont("arial", 50)

    def input(self, event: pygame_event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.index = (self.index - 1) % len(self.items)
            if event.key == K_DOWN:
                self.index = (self.index + 1) % len(self.items)
            if event.key == K_RETURN:
                if self.index == 0:
                    self.manager.new_state(OnePlayerOneHead(self.field))
                elif self.index == 1:
                    self.manager.new_state(OnePlayerTwoHead(self.field))
                elif self.index == 2:
                    self.manager.new_state(TwoPlayerOneHead(self.field))
                elif self.index == 3:
                    self.manager.new_state(TwoPlayerTwoHead(self.field))

    def draw(self, screen: Surface):
        self.field.draw(screen)
        for i in range(len(self.items)):
            print(i)
            color = (0, 0, 0)
            if i == self.index:
                color = (255, 255, 255)
            str_width, str_height = self.item_font.size(self.items[i])
            self.draw_string(screen, self.items[i], self.item_font, color,
                             (screen.get_width() - str_width) // 2,
                             int(screen.get_height() * (i + 1) / (len(self.items) + 1) - str_height / 2))

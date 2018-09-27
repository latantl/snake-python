from mysnake.utils.statemanager import *


# abstract
class State:

    def __init__(self):
        self.manager: StateManager = None

    # abstract
    def input(self, event: pygame_event):
        pass

    # abstract
    def draw(self, screen: Surface):
        pass

    # abstract
    def on_run(self):
        pass

    def draw_string(self, screen: Surface, string, font, color, x: int, y: int):
        label = font.render(string, 1, color)
        screen.blit(label, (x, y))
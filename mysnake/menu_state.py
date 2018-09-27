from mysnake.utils.state import *


class MenuState(State):

    def __init__(self):
        self.menu_items: dict[int, State] = dict()

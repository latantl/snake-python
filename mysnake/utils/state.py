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
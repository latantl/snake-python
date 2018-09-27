from pygame import Surface
from pygame import event as pygame_event


class StateManager:

    def __init__(self, first_state):
        self.state_stack = [first_state]
        first_state.manager = self

    @property
    def actual_state(self):
        return self.state_stack[len(self.state_stack) - 1]

    def input(self, event: pygame_event):
        self.actual_state.input(event)

    def draw(self, screen: Surface):
        self.actual_state.draw(screen)

    def on_run(self):
        self.actual_state.on_run()

    def go_back(self):
        if len(self.state_stack) != 1:
            self.state_stack.pop()

    def new_state(self, state):
        self.state_stack.append(state)
        state.manager = self

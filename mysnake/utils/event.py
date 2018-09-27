
class Event:

    def __init__(self):
        self.handlers: [function] = []

    def sub(self, handler):
        self.handlers.append(handler)

    def un_sub(self, handler):
        self.handlers.remove(handler)

    def fire(self, earg):
        for h in self.handlers:
            h(earg)

from mysnake.snake.wall import *


class WalledField(Field):

    def build_walls(self):
        Wall(self, Vec(self.size - 1, self.size - 1))
        Wall(self, Vec(0, self.size - 1))
        Wall(self, Vec(self.size - 1, 0))
        Wall(self, Vec(0, 0))
        for i in range(1, self.size // 3 - 1):
            coords = [[0, self.size - 1], [i, self.size - 1 - i]]
            for j in coords[0]:
                for k in coords[1]:
                    Wall(self, Vec(j, k))
                    Wall(self, Vec(k, j))
            # equivalent to:
            # Wall(self, Vec(i, 0))
            # Wall(self, Vec(i, self.size - 1))
            # Wall(self, Vec(self.size - 1 - i, 0))
            # Wall(self, Vec(self.size - 1 - i, self.size - 1))
            # Wall(self, Vec(0, i))
            # Wall(self, Vec(self.size - 1, i))
            # Wall(self, Vec(0, self.size - 1 - i))
            # Wall(self, Vec(self.size - 1,self. size - 1 - i))


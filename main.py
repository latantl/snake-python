from mysnake.one_player_one_head import *
from mysnake.menu_state import MenuState
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SIZE = (660, 660)

pygame.init()
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Snake")
DONE = False
CLOCK = pygame.time.Clock()

manager = StateManager(MenuState())

while not DONE:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True
        manager.input(event)

    manager.on_run()
    manager.draw(SCREEN)

    pygame.display.flip()
    CLOCK.tick(60)

pygame.quit()

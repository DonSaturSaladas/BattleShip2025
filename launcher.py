import pygame
from views.view_constants import *
from views.main_screen import MainScreen

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
main_screen = MainScreen(screen)

while main_screen.is_running():
    main_screen.run()

pygame.quit()

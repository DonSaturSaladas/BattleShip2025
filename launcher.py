import pygame
from controller.game import Game
from views.view_constants import SCREEN_WIDTH, SCREEN_HEIGHT
from views.main_screen import MainScreen

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
main_screen = MainScreen(screen)
game = Game(main_screen)
main_screen.game = game
while main_screen.is_running():
    main_screen.run()

pygame.quit()

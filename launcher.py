import pygame
from controller.game import Game
from views.view_constants import BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT
from views.main_screen import Main_Screen

pygame.init()
screen = pygame.display.set_mode((BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT), pygame.RESIZABLE)
main_screen = Main_Screen(screen)
game = Game(main_screen)
main_screen.game = game
while main_screen.is_running():
    main_screen.run()

pygame.quit()

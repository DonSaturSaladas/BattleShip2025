import pygame
from view_constants import *
from ship_setup_screen import ShipSetupScreen

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ship_setup_screen = ShipSetupScreen(screen)

selected_screen = ship_setup_screen

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    selected_screen.run()
    pygame.display.update()

pygame.quit()
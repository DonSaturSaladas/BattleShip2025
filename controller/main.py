import pygame

WIN = pygame.display.set_mode((1080, 1920))
pygame.display.set_caption("battleship2025")






def main():
    run = true;
    clock = pygame.time.Clock()
    game = Game(WIN)
    

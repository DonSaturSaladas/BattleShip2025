import pygame
from views.view_constants import CELL_SIZE, BOARD_SEPARATION


class CellObserver:
    def __init__(self, win, cell):
        self.win = win
        self.sprite = cell.actualSprite
        self.cell = cell

        self.rx = self.calcPos(self.cell.x)
        self.ry = self.calcPos(self.cell.y)

    def update(self):
        self.win.window.blit(self.sprite.getImg(), (self.rx, self.ry))
        pygame.display.update()

    def setSprite(self, sprite):
        self.sprite = sprite

    def calcPos(self, value):
        return CELL_SIZE * value + BOARD_SEPARATION


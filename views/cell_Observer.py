import pygame
from views.view_constants import CELL_SIZE, BOARD_SEPARATION
from views.main_screen import Main_Screen
from controller.factories.sprite import Sprite

class Cell_Observer:
    def __init__(
        self,
        win,
        cell,
    ):
        self.win:Main_Screen = win
        self.sprite :Sprite = cell.actualSprite
        self.cell = cell

        self.rx = self.calcPos(self.cell.x)
        self.ry = self.calcPos(self.cell.y)

    def update(self, left, top):
        self.sprite.path = pygame.transform.scale((self.sprite.getImg()),(self.win.scaled_cell_size -3, self.win.scaled_cell_size-1))
        self.rx = self.calcPos(self.cell.x)
        self.ry = self.calcPos(self.cell.y)
        self.win.window.blit(self.sprite.getImg(), (self.rx + left, self.ry + top))
        pygame.display.update()


    def setSprite(self, sprite):
        self.sprite = sprite

    def calcPos(self, value):
        return self.win.scaled_cell_size * value 

import pygame
from views.view_constants import CELL_SIZE, BOARD_SEPARATION
from views.main_screen import Main_Screen
from controller.factories.sprite import Sprite

class Cell_Observer:
    def __init__(self,win,cell):
        self.win:Main_Screen = win
        self.sprite :Sprite = cell.actualSprite
        self.cell = cell

        self.relative_x = self.cell.x
        self.relative_y = self.cell.y
        self.calcPos(0,0)

    def update(self, left, top):
        self.sprite.path = pygame.transform.scale((self.sprite.getImg()),(self.win.scaled_cell_size -3, self.win.scaled_cell_size-1))
        
        self.calcPos(left,top)
        
        self.win.window.blit(self.sprite.getImg(), (self.relative_x , self.relative_y))


    def setSprite(self, sprite):
        self.sprite = sprite

    def calcPos(self, left, top):
        self.relative_x = self.win.scaled_cell_size * self.cell.x + left
        self.relative_y = self.win.scaled_cell_size * self.cell.y + top 

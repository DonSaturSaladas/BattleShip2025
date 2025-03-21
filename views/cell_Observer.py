import pygame
from views.view_constants import CELL_SIZE, BOARD_SEPARATION
from views.main_screen import Main_Screen
from controller.factories.sprite import Sprite
from .observers import Object_observer

class Cell_Observer():
    def __init__(self,main_screen,cell):
        self.win:Main_Screen = main_screen
        self.cell = cell

        self.relative_x = self.cell.x
        self.relative_y = self.cell.y
        self.calcPos(0,0)

    def update(self, left = None, top = None):
        #Cuidado cuando implementamos las skins de los barcos con el surface
        self.cell.actualSprite.path = pygame.transform.scale((self.cell.actualSprite.getImg()),(self.win.scaled_cell_size -3, self.win.scaled_cell_size-1))
        if left is not None and top is not None:
            self.calcPos(left,top)
        
        self.win.window.blit(self.cell.actualSprite.getImg(), (self.relative_x , self.relative_y))


    

    def calcPos(self, left, top):
        self.relative_x = self.win.scaled_cell_size * self.cell.x + left
        self.relative_y = self.win.scaled_cell_size * self.cell.y + top 

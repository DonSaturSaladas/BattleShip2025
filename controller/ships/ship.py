from abc import ABC, abstractmethod
from controller.board_elements.cell import Cell
from controller.factories.sprite import Sprite
from views.view_constants import *

class Ship():
    
    def __init__(self, cells): 
        self.parts: list[Cell]  = cells
        status = "hidden"
        sunked = False
        self.init_ship_parts()
        
        
    def init_ship_parts(self):
        #Cambiar skin de cada celda del barco
        for cell in self.parts:
            cell.hasShip = True
            cell.changeSprite(Sprite(SHIP_TEST_PATH))
            cell.update()
        
        
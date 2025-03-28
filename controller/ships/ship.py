from abc import ABC, abstractmethod
from controller.board_elements.cell import Cell
from controller.factories.sprite import Sprite
from views.view_constants import *

class Ship():
    
    def __init__(self, cells): 
        self.parts: list[Cell]  = cells
        self.status = "hidden"
        self.sunked = False
        self.init_ship_parts()
        self.hits = 0
        
        
    def init_ship_parts(self):
        #Cambiar skin de cada celda del barco
        for cell in self.parts:
            cell.hasShip = True
            cell.changeSprite(Sprite(SHIP_TEST_PATH))
            cell.update()
    
    def has_cell(self, cell):
        has_cell = False
        part_index = 0
        while not has_cell and part_index < len(self.parts):
            if cell == self.parts[part_index]:
                has_cell = True
            part_index += 1
        return has_cell

    def hit(self, cell):
        self.hits += 1
        if self.hits == len(self.parts):
            self.sunked = True
            print(f'Size {len(self.parts)} sunked')
            
    def get_length(self):
        return len(self.parts)
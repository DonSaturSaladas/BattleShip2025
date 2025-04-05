from .ship import Ship
from views.view_constants import *

from views.spritesheet import spritesheet

class Battleship(Ship):
    
    def __init__(self, cells):
        super().__init__(cells)
        
    def init_ship_sprite(self, path, width, height):
        super().init_ship_sprite(BATTLESHIP_PATH, 500, 500)
    
           
            
        
        
    
    
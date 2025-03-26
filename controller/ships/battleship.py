from .ship import Ship

class Battleship(Ship):
    
    def __init__(self, cells):
        super().__init__(cells)
        
    def init_ship_parts(self):
        pass
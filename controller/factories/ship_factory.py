from controller.ships import *

class Ship_factory:
    
    def __init__(self):
        self.ship_clases ={
            5 : Carrier, 
            4 : Battleship,
            3 : {
                "Cruiser" : Cruiser, 
                "Submarine" : Submarine,
                None : Cruiser
            }, 
            2: Destroyer  
        }
    
    def create_ship(self, cells:[], ship_type = None):
        ship_size = len(cells)
        if  ship_size not in self.ship_clases:
            raise ValueError(f"No existe un barco de esa longitud {ship_size}")

        if(ship_size == 3):
            ship_class = self.ship_clases[ship_size].get(ship_type, self.ship_clases[ship_size][None])
        else:
            ship_class = self.ship_clases[ship_size]

        return ship_class(cells)
        

        
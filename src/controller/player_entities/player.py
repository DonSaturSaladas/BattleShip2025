from .player_entity import Player_Entity

class Player(Player_Entity):
    
    def __init__(self):
        super().__init__()
        self.show_ship_pos()
        
    def getBoard(self):
        return super().getBoard()
    
    
    def put_ship(self, ship):
        return super().put_ship(ship)
    
    def play(self):
        pass
    
    def show_ship_pos(self):
        for ship in self.ships:
            ship.show_cells()
    
from .player_entity import Player_Entity

class Player(Player_Entity):
    
    def __init__(self):
        super().__init__()
        
    def getBoard(self):
        return super().getBoard()
    
    
    def put_ship(self, ship):
        return super().put_ship(ship)
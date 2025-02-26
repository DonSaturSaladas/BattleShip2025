from board import Board

class PlayerEntity:
    def __init__(self):
        self.board = Board()
        self.ships = []
        
    def putShip(self, ship):
        
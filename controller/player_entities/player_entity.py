from controller.board_elements.board import Board
from abc import ABC, abstractmethod

class Player_Entity(ABC):
    
    def __init__(self):
        self.board = Board()
        self.ships = [] 

    @abstractmethod
    def put_ship(self, ship):
        self.ships.append(ship)

    @abstractmethod
    def getBoard(self):
        return self.board
    
     

from controller.board_elements.board import Board
from abc import ABC, abstractmethod

class Player_Entity(ABC):
    
    def __init__(self):
        self.board = Board()
        self.ships = []
        self.remaining_ships = 0

    @abstractmethod
    def put_ship(self, ship):
        self.ships.append(ship)
        self.remaining_ships += 1

    @abstractmethod
    def getBoard(self):
        return self.board
    
    def shoot_cell(self, cell_x, cell_y):
        ship_hitted = False
        cell = self.board.getCell(cell_x, cell_y)
        self.board.shoot_cell(cell)
        if cell.hasShip:
            self.hit_ship(cell)
            ship_hitted = True
        return ship_hitted
            
    
    def hit_ship(self, cell):
        found_ship_cell = False
        ship_index = 0
        while not found_ship_cell and ship_index < len(self.ships):
            ship = self.ships[ship_index]
            if ship.has_cell(cell):
                ship.hit(cell)
                if ship.sunked:
                    self.sunk_ship()
            ship_index += 1

    def sunk_ship(self):
        self.remaining_ships -= 1
        if self.remaining_ships == 0:
            print("No ships remaining")

     
    def can_shoot_cell(self, cell):
        return cell.hidden
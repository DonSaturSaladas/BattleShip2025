from pygame import Rect

class Ship_Placeholder:
    def __init__(self, pool_coordinates, ship_length, cell_size):
        self.base_x = pool_coordinates[0]
        self.base_y = pool_coordinates[1]
        self.rectangle = Rect(self.base_x, self.base_y, ship_length * cell_size, cell_size)
        self.board_coordinates = None
    
    def set_board_coordinates(self, board_x, board_y):
        self.board_coordinates = (board_x, board_y)
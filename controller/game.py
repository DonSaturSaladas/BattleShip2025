from player_entities import player_entity
from views.view_constants import * 

class Game:
    def __init__(self, main_screen):
        self.player = player_entity()
        self.main_screen = main_screen
        
        
    def setPlayerObserver(self):
        for row in range(ROWS):
            for col in range (COLS):
                self.player.board.cells[row][col]
    
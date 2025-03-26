import random

from player_entity import Player_Entity
from views.view_constants import *


MODES = ["Target", "Hunt"]

class Opponent_ai(Player_Entity):
    
    def __init__(self, game):
        self.game = game
        self.mode = MODES[0]
        self.game.init_ai_coords()
        super().__init__()
    
    
    def play():
        pass
    
    
        
    def make_guess(self):
        if self.mode == "Hunt":
            target_coords = self.generate_random_coords()
            self.game.player.shoot_cell(target_coords[0], target_coords[1])
        else:
            pass
            
            
            
    def hunt_mode(self):
        self.mode = "Hunt"
        
    def target_mode(self):
        self.mode = "Target"
        
    def generate_random_coords(self):
        
        random_coords = random.randint(0, ROWS) , random.randint(0, COLS)
        
        while not self.game.can_shoot_cell(self.game.player.board.getCell(random_coords[0],random_coords[1])):
            random_coords = random.randint(0, ROWS) , random.randint(0, COLS)
            
        return random_coords
        
        
    
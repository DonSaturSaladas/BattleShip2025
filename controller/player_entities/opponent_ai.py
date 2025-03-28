import random

from .player_entity import Player_Entity
from views.view_constants import *

from controller.board_elements.board import Board


MODES = ["Target", "Hunt"]

class Opponent_ai(Player_Entity):
    
    def __init__(self, game):
        self.game = game
        self.mode = MODES[0] # HUNT or TARGET
        
        self.probability_matrix = [] # Auxiliar matrix for the probabilitys
        self.enemy_alive_ships = game.player.ships # Player alive ships
        self.init_matrix()
        self.last_hited_cell = None # For target mode knowledge
        
        
        
        
        super().__init__()
    
    
    
    def init_matrix(self):
        for row in range(ROWS):
            self.probability_matrix.append([])
            for col in range(COLS):
                self.probability_matrix[row].append(0)
                
        print(self.probability_matrix)
                
                
                
                
    def play(self):
        pass
    
    def getBoard(self):
        return super().getBoard()
    
    def put_ship(self, ship):
        return super().put_ship(ship)
        
    def make_guess(self):
        player = self.game.player
        
        if self.mode == "Hunt":
            self.dfs_hunt()
                
        elif self.mode == "Target":
            self.dfs_target()
    
    def dfs_hunt(self):
        pass
    
    def update_probabilty_matrix(self):
        player_board :Board = self.game.player.board
        self.clean_probability_matrix()
        if self.mode == "Hunt":
            self.update_probability_matrix_hunt(player_board)
        elif self.mode == "Target":
            self.update_probability_matrix_target(player_board)
    
    def update_probability_matrix_target(self, player_board):
        hited_cell_x = self.last_hited_cell.x
        hited_cell_y = self.last_hited_cell.y
        
        for ship in self.enemy_alive_ships:
            
            #Check horizontal probable disposition of ship from the last_hited_cell
            for i in range (1, len(ship)):
                pass
                
                
                            
    def update_probability_matrix_hunt(self, player_board):
        
        for ship in self.enemy_alive_ships: # For each player has alive calculate the prob
            
        #Check horizontal probable disposition of ship
            for row in range(ROWS):
                for col in range(COLS):
                    
                    valid_pos = True
                    if(player_board.getCell.x + len(ship) < ROWS):
                        valid_pos = False
                        
                    i = 0
                    while i < len(ship) and valid_pos:
                        if not player_board.getCell(row, col + i).is_hidden():
                            valid_pos = False
                            break
                        i += 1
                    if valid_pos:
                        for j in range(len(ship)):
                            self.probability_matrix[row][col + i] += 1
                            
                    else:
                        valid_pos = True
                        
            #Check vertical probable disposition of ship
            for row in range(ROWS):
                for col in range(COLS):
                    
                    valid_pos = True
                    if(player_board.getCell.y + len(ship) < COLS):
                        valid_pos = False
                        
                    j = 0
                    while j < len(ship) and valid_pos:
                        if not player_board.getCell(row + j, col).is_hidden():
                            valid_pos = False
                            break
                        j += 1
                        
                    if valid_pos:
                        for j in range(len(ship)):
                            self.probability_matrix[row + i][col] += 1     
                    else:
                        valid_pos = True
    
        
    
    
    def clean_probability_matrix(self):
        for row in ROWS:
            for col in COLS:
                self.probability_matrix[row][col] = 0
            
            
            
    def hunt_mode(self):
        self.mode = "Hunt"
        
    def target_mode(self):
        self.mode = "Target"
        
    def generate_random_coords(self):
        
        random_coords = random.randint(0, ROWS) , random.randint(0, COLS)
        
        while not self.game.player.can_shoot_cell(self.game.player.board.getCell(random_coords[0],random_coords[1])):
            random_coords = random.randint(0, ROWS) , random.randint(0, COLS)
            
        return random_coords






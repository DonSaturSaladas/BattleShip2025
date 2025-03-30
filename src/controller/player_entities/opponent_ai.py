import random

from .player_entity import Player_Entity
from views.view_constants import *

from controller.board_elements.board import Board


MODES = ["Target", "Hunt"]

class Opponent_ai(Player_Entity):
    
    def __init__(self, game):
        self.game = game
        self.mode = MODES[1] # HUNT or TARGET
        
        self.probability_matrix = [] # Auxiliar matrix for the probabilitys
        self.enemy_alive_ships = game.player.ships # Player alive ships
        self.init_matrix()

        self.target_mode_hited_cells = [] # For target mode knowledge
        
        
        
        
        super().__init__()
    
    
    
    def init_matrix(self):
        for row in range(ROWS):
            self.probability_matrix.append([])
            for col in range(COLS):
                self.probability_matrix[row].append(0)
                
        print(self.probability_matrix)
                
                
                           
    def play(self):
        if(self.game.player.remaining_ships > 0):
            #print(self.game.player.remaining_ships)
            self.make_guess()
            self.game.change_current_player()
            print("Player changed")   
    
    def getBoard(self):
        return super().getBoard()
    
    def put_ship(self, ship):
        return super().put_ship(ship)
        
    def make_guess(self):
        player = self.game.player
        if self.mode == "Hunt":
            self.dfs_hunt(player)
                
        elif self.mode == "Target":
            self.dfs_target(player)
    
    def dfs_hunt(self, player):
        print("enter Hunt mode")
        self.update_probability_matrix()
        target_cell = self.get_most_probable_cell()
        hit, sunked =  player.shoot_cell(target_cell.x, target_cell.y)
        self.print_prob_matrix()
        
        if(hit):
            self.target_mode()
            
            self.target_mode_hited_cells.append(target_cell)
        
        
    
    def dfs_target(self, player):
        print("enter Target mode")
        self.update_probability_matrix()
        target_cell = self.get_most_probable_cell()
        hit, sunked =  player.shoot_cell(target_cell.x, target_cell.y)
        self.print_prob_matrix()
        if(hit):
            self.target_mode_hited_cells.append(target_cell)
        
        if(sunked):
            
            self.enemy_alive_ships = [ship for ship in player.ships if not ship.sunked] #Cambiar sentencia No se actualizan correctamente los barcos vivos
            print(len(self.enemy_alive_ships))
            self.target_mode_hited_cells = []
            self.hunt_mode()
    
    
        
    
    def update_probability_matrix(self):
        player_board :Board = self.game.player.board
        self.clean_probability_matrix()
        if self.mode == "Hunt":
            self.update_probability_matrix_hunt(player_board)
        elif self.mode == "Target":
            self.update_probability_matrix_target(player_board)
    
    def update_probability_matrix_target(self, player_board):
        hited_cell_x = self.target_mode_hited_cells[len(self.target_mode_hited_cells)-1].x
        hited_cell_y = self.target_mode_hited_cells[len(self.target_mode_hited_cells)-1].y
        
        for ship in self.enemy_alive_ships:
            
            #Check horizontal to the  probable disposition of ship from the last_hited_cell
            for x in range (1-ship.get_length(), ship.get_length()):
                
                posible_ship = []
                valid_pos = True
                current_cell_x = x + hited_cell_x
                
                if ( current_cell_x < 0 or current_cell_x +ship.get_length() >= ROWS):
                    valid_pos = False
                    
                i = 0
                while i < ship.get_length() and valid_pos:
                    cell = player_board.getCell(current_cell_x + i, hited_cell_y)
                    posible_ship.append(cell)
                    if (not cell.is_hidden()):
                        if cell in self.target_mode_hited_cells:
                            pass
                        else:
                            valid_pos = False
                            
                            break
                    i += 1
                
                if(not self.contains_all_elements(self.target_mode_hited_cells, posible_ship) and not valid_pos):
                    valid_pos = False
                    
                if valid_pos:
                    for j in range(ship.get_length()):
                        if(not player_board.getCell(current_cell_x +j, hited_cell_y) in self.target_mode_hited_cells):
                            self.probability_matrix[hited_cell_y][current_cell_x + j] += 1
                    
                        
            
            #Check vertically to the probable disposition of ship from the last_hited_cell
            for y in range (1-ship.get_length(), ship.get_length()):
                
                posible_ship = []
                valid_pos = True
                current_cell_y = y + hited_cell_y
                
                if (current_cell_y < 0 or current_cell_y +ship.get_length() >= COLS):
                    valid_pos = False
                    
                i = 0
                while i < ship.get_length() and valid_pos:
                    cell = player_board.getCell(hited_cell_x, current_cell_y + i)
                    posible_ship.append(cell)
                    if (not cell.is_hidden()):
                        if cell in self.target_mode_hited_cells:
                            pass
                        else:
                            valid_pos = False
                            break
                    i += 1
                
                if(not self.contains_all_elements(self.target_mode_hited_cells, posible_ship) and not valid_pos):
                    valid_pos = False
        
                if valid_pos:
                    for j in range(ship.get_length()):
                        if(not player_board.getCell(hited_cell_x, current_cell_y + j) in self.target_mode_hited_cells):
                            self.probability_matrix[current_cell_y + j][hited_cell_x] += 1
                        
                    
                    
                    
                    
                        
                        
                
                
                            
    def update_probability_matrix_hunt(self, player_board):
        
        for ship in self.enemy_alive_ships: # For each player has alive calculate the prob
            
        #Check horizontal probable disposition of ship
            for row in range(ROWS):
                for col in range(COLS):
                    
                    valid_pos = True
                    if(col + ship.get_length() >= ROWS):
                        valid_pos = False
                        
                    i = 0
                    while i < ship.get_length() and valid_pos:
                        if not player_board.getCell(col + i, row).is_hidden():
                            valid_pos = False
                            break
                        i += 1
                        
                    if valid_pos:
                        for j in range(ship.get_length()):
                            self.probability_matrix[row][col + j] += 1
                            
                    else:
                        valid_pos = True
                        
            #Check vertical probable disposition of ship
            for row in range(ROWS):
                for col in range(COLS):
                    
                    valid_pos = True
                    if(row + ship.get_length() >= COLS):
                        valid_pos = False
                        
                    j = 0
                    while j < ship.get_length() and valid_pos:
                        if not player_board.getCell(col, row + j).is_hidden():
                            valid_pos = False
                            break
                        j += 1
                        
                    if valid_pos:
                        for j in range(ship.get_length()):
                            self.probability_matrix[row + j][col] += 1     
                    else:
                        valid_pos = True
    
        
    
    
    def clean_probability_matrix(self):
        for row in range(ROWS):
            for col in range(COLS):
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

    def contains_all_elements(self, list1, list2):
        return set(list1) <= set(list2)

    def get_most_probable_cell(self):
        max_value = max(max(row) for row in self.probability_matrix)
        player_board = self.game.player.board
        # Get all coordinates with max probability using list comprehension
        max_coords = [player_board.getCell(j,i) for i in range(len(self.probability_matrix)) 
                     for j in range(len(self.probability_matrix[0])) 
                     if self.probability_matrix[i][j] == max_value]
        
        # Return random coordinate from the max probability cells
        return random.choice(max_coords)

    
    def print_prob_matrix(self):
        for row in range(ROWS):
            row_str = ""
            for col in range(COLS):
                # Format each number to take up 3 spaces, right-aligned
                row_str += f"{self.probability_matrix[row][col]:3} "
            print(row_str)

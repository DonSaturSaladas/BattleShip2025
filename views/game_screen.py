from .view_constants import *

class GameScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.game = None
        self.scaled_cell_size = main_screen.scaled_cell_size

        self.boards_coordinates = None
    
    def set_game(self, game):
        self.game = game
        self.boards_coordinates = self.get_players_board_coordinates()

    def run(self):
        self.draw_player_board()
        self.draw_enemy_board()
        self.game.run_game()
    
    def draw_player_board(self):
        player_left, player_top = self.boards_coordinates[self.game.player]
        self.main_screen.draw_board(player_left, player_top, self.game.player.board)
    
    def draw_enemy_board(self):
        enemy_left, enemy_top = self.boards_coordinates[self.game.opponent_ai]
        self.main_screen.draw_board(enemy_left, enemy_top, self.game.opponent_ai.board)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_clicked(event)
    
    def mouse_clicked(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        if event.button == 1:    #Left Click
            if self.clicked_current_player_board(mouse_x, mouse_y):
                player = self.game.get_current_player()
                clicked_cell = self.get_current_player_clicked_cell(mouse_x, mouse_y)
                clicked_cell_coords = (clicked_cell.x , clicked_cell.y)
                
                if player.can_shoot_cell(clicked_cell):
                    player.shoot_cell(clicked_cell_coords[0], clicked_cell_coords[1])
                    self.game.change_current_player()
    
    def clicked_current_player_board(self, coord_x, coord_y):
        x_on_board = coord_x >= self.boards_coordinates[self.game.current_player][0] and coord_x <= self.boards_coordinates[self.game.current_player][0] + ROWS * self.scaled_cell_size
        y_on_board = coord_y >= self.boards_coordinates[self.game.current_player][1] and coord_y <= self.boards_coordinates[self.game.current_player][1] + COLS * self.scaled_cell_size
        return x_on_board and y_on_board
    
    
    def get_current_player_clicked_cell(self, coord_x, coord_y):
        board_x = int((coord_x - self.boards_coordinates[self.game.current_player][0]) // self.scaled_cell_size)
        board_y = int((coord_y - self.boards_coordinates[self.game.current_player][1]) // self.scaled_cell_size)
        return self.game.current_player.board.getCell(board_x, board_y)
    

    def get_players_board_coordinates(self):
        used_width = ROWS * self.scaled_cell_size * 2 + BOARD_SEPARATION
        used_height = COLS * self.scaled_cell_size
        left_padding = (self.main_screen.screen_width - used_width) / 2
        top_padding = (self.main_screen.screen_height - used_height) / 2
        left_player_board_coordinates = (left_padding, top_padding)
        right_player_board_coordinates = (left_padding + BOARD_SEPARATION + ROWS * self.scaled_cell_size, top_padding)
        
        return {self.game.player : left_player_board_coordinates, 
                self.game.opponent_ai : right_player_board_coordinates}

    def screen_size_changed(self):
        self.scaled_cell_size = self.main_screen.scaled_cell_size
        self.boards_coordinates = self.get_players_board_coordinates()
        
    
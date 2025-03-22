from .view_constants import *

class GameScreen:
    def __init__(self, window, main_screen):
        self.window = window
        self.main_screen = main_screen
        self.game = None
        self.scaled_cell_size = main_screen.scaled_cell_size
        self.current_player = 0 #0 = player, 1 = Computer
        self.boards_coordinates = self.get_players_board_coordinates()
    
    def set_game(self, game):
        self.game = game

    def run(self):
        self.draw_player_board()
        self.draw_enemy_board()
    
    def draw_player_board(self):
        player_left, player_top = self.boards_coordinates[0]
        self.main_screen.draw_board(player_left, player_top, self.game.player.board)
    
    def draw_enemy_board(self):
        enemy_left, enemy_top = self.boards_coordinates[1]
        self.main_screen.draw_board(enemy_left, enemy_top, self.game.opponent_ai.board)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mouse_clicked(event)
    
    def mouse_clicked(self, event):
        mouse_x = event.pos[0]
        mouse_y = event.pos[1]
        if event.button == 1:    #Left Click
            if self.clicked_current_player_board(mouse_x, mouse_y):
                player = self.get_current_player()
                clicked_cell_coords = self.get_current_player_clicked_cell(mouse_x, mouse_y)
                if self.can_shoot_cell(clicked_cell_coords):
                    self.shoot_cell(clicked_cell_coords, player)
                    self.change_current_player()
    
    def clicked_current_player_board(self, coord_x, coord_y):
        x_on_board = coord_x >= self.boards_coordinates[self.current_player][0] and coord_x <= self.boards_coordinates[self.current_player][0] + ROWS * self.scaled_cell_size
        y_on_board = coord_y >= self.boards_coordinates[self.current_player][1] and coord_y <= self.boards_coordinates[self.current_player][1] + COLS * self.scaled_cell_size
        return x_on_board and y_on_board
    
    def get_current_player(self):
        return self.game.player if self.current_player == 0 else self.game.opponent_ai

    def get_current_player_clicked_cell(self, coord_x, coord_y):
        board_x = int((coord_x - self.boards_coordinates[self.current_player][0]) // self.scaled_cell_size)
        board_y = int((coord_y - self.boards_coordinates[self.current_player][1]) // self.scaled_cell_size)
        return (board_x, board_y)
    
    def can_shoot_cell(self, cell_coords):
        cell = self.get_current_player().board.getCell(cell_coords[0], cell_coords[1])
        return cell.hidden
    
    def shoot_cell(self, coordinates, player_entity):
        player_entity.shoot_cell(coordinates[0], coordinates[1])
    
    def change_current_player(self):
        self.current_player = 0 if self.current_player == 1 else 1
    

    def get_players_board_coordinates(self):
        used_width = ROWS * self.scaled_cell_size * 2 + BOARD_SEPARATION
        used_height = COLS * self.scaled_cell_size
        left_padding = (self.main_screen.screen_width - used_width) / 2
        top_padding = (self.main_screen.screen_height - used_height) / 2
        left_player_board_coordinates = (left_padding, top_padding)
        right_player_board_coordinates = (left_padding + BOARD_SEPARATION + ROWS * self.scaled_cell_size, top_padding)
        return [left_player_board_coordinates, right_player_board_coordinates]

    def screen_size_changed(self):
        self.scaled_cell_size = self.main_screen.scaled_cell_size
        self.boards_coordinates = self.get_players_board_coordinates()
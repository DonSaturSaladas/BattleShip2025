import pygame
from .ship_setup_screen import ShipSetupScreen
from .game_screen import GameScreen
from .menu_screen import Menu_screen
from .view_constants import (
    CELL_SIZE,
    ROWS,
    COLS,
    BASE_SCREEN_HEIGHT,
    BASE_SCREEN_WIDTH
)


class Main_Screen:
    def __init__(self, window):
        
        # WIN variables
        self.running = True
        self.window = window
        self.screen_width, self.screen_height = pygame.display.get_surface().get_size()
        self.scale_factor = 1
        self.scaled_cell_size = int(CELL_SIZE * self.scale_factor)

        # SCREEN variables
        self.ship_setup_screen = None
        self.game_screen = None
        self.setup_screens()
        
        self.first_iteration = True
        self.game = None
        self.PRIMARY_FONT = pygame.font.SysFont('ArcadeClassic', 30, True, False)

    def set_game(self, game):
        self.game = game
        self.game_screen.set_game(game)

    def run(self):
        self.window.fill((0,0,0,0))

        self.selected_screen.run()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.VIDEORESIZE:
                nWidth, nHeight = event.w, event.h
                self.scale_factor = nWidth / BASE_SCREEN_WIDTH
                self.scaled_cell_size = int(CELL_SIZE * self.scale_factor)
                self.window = pygame.display.set_mode(
                    (nWidth, nHeight), pygame.RESIZABLE
                )
                self.screen_width = nWidth
                self.screen_height = nHeight
                self.screen_size_changed()
                
            self.selected_screen.handle_event(event)

        self.first_iteration = False
        pygame.display.update()

    def screen_size_changed(self):
        self.ship_setup_screen.screen_size_changed()
        self.game_screen.screen_size_changed()
        
    def is_running(self):
        return self.running

    def change_screen(self, screen : str):
        if(screen == "Game"):
            self.selected_screen = self.game_screen
        elif(screen == "Menu"):
            self.selected_screen = self.menu_screen
        elif(screen == "Setup"):
            self.selected_screen = self.ship_setup_screen
        elif(screen == "GameOver"):
            self.selected_screen = self.game_over_screen
        elif(screen == "LeaderBoard"):
            self.selected_screen = self.leaderboard_screen
    
    
    def setup_screens(self):
        self.menu_screen = Menu_screen(self.window, self)
        self.ship_setup_screen = ShipSetupScreen(self.window, self)
        self.game_screen = GameScreen(self.window, self)
        # self.game_over_screen = GameOverScreen(window, self)
        # self.leaderboard_screen = LeaderBoardScreen(window, self)
        self.selected_screen = self.menu_screen #Later change to menu screen
        
        
    def draw_board(self, left, top, num_pos, board=None):
        board_width = ROWS * self.scaled_cell_size
        board_height = COLS * self.scaled_cell_size

        pygame.draw.rect(
            self.window,
            (255, 255, 255),
            pygame.Rect(left, top, board_width, board_height),
            width=1,
        )
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(
                    self.window,
                    (255, 255, 255),
                    pygame.Rect(
                        row * self.scaled_cell_size + left,
                        col * self.scaled_cell_size + top,
                        self.scaled_cell_size,
                        self.scaled_cell_size,
                    ),
                    width=1,
                )

                if board:
                    board.getCell(row, col).observer.set_pos(left, top)
                    board.getCell(row, col).observer.update()  # TODO : replace with a way to choose whose board draw (player or opponent)
                    
        for col in range(ROWS):
            letter = chr(65 + col)  # 65 es el código ASCII de 'A'
            text_surface = self.PRIMARY_FONT.render(letter, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            # Centra la letra en la celda correspondiente
            text_rect.centerx = left + (col * self.scaled_cell_size) + (self.scaled_cell_size // 2)
            text_rect.bottom = top - 5  # Ajusta el margen superior (por ejemplo, 5 píxeles arriba)
            self.window.blit(text_surface, text_rect)

        # Dibuja los números (1 a 10) a la izquierda del tablero.
        for row in range(COLS):
            number = str(row + 1)
            text_surface = self.PRIMARY_FONT.render(number, True, (255, 255, 255))
            text_rect = text_surface.get_rect()
            # Centra el número en la vertical correspondiente
            text_rect.centery = top + (row * self.scaled_cell_size) + (self.scaled_cell_size // 2)
            if num_pos == "L":
                text_rect.right = left - 5  
            else:
                text_rect.left = left + board_width + 5
                
            self.window.blit(text_surface, text_rect)


    """def draw_ship(self, lenght, left, top, color):
        pygame.draw.rect(
            self.window, color, pygame.Rect(left, top, lenght * self.scaled_cell_size, self.scaled_cell_size)
        )"""
        

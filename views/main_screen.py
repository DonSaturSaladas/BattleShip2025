import pygame
from .ship_setup_screen import ShipSetupScreen
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
        
        self.game = None
        self.PRIMARY_FONT = pygame.font.SysFont('arial', 25, True, False)

    def run(self):
        self.window.fill((0, 0, 0))

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
                self.ship_setup_screen.screen_size_changed()
                
            self.selected_screen.handle_event(event)

        self.selected_screen.run()
        pygame.display.update()

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
        #self.menu_screen = MenuScreen(window, self)
        self.ship_setup_screen = ShipSetupScreen(self.window, self)
        # self.game_screen = Game_Screen(window, self)
        # self.game_over_screen = GameOverScreen(window, self)
        # self.leaderboard_screen = LeaderBoardScreen(window, self)
        self.selected_screen = self.ship_setup_screen #Later change to menu screen
        
        
    def draw_board(self, left, top):
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

                self.game.player.board.getCell(row, col).update(
                    left, top
                )  # TODO : replace with a way to choose whose board draw (player or opponent)


    """def draw_ship(self, lenght, left, top, color):
        pygame.draw.rect(
            self.window, color, pygame.Rect(left, top, lenght * self.scaled_cell_size, self.scaled_cell_size)
        )"""
        

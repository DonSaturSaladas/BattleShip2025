import pygame
from .ship_setup_screen import ShipSetupScreen
from .view_constants import (
    CELL_SIZE,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    SCREEN_WIDTH,
    ROWS,
    COLS,
)


class MainScreen:
    def __init__(self, window):
        self.running = True
        self.window = window
        self.ship_setup_screen = ShipSetupScreen(window, self)
        self.selected_screen = self.ship_setup_screen
        self.scale_factor = 1
        self.scaled_cell_size = int(CELL_SIZE * self.scale_factor)
        self.game = None

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.VIDEORESIZE:
                nWidth, nHeight = event.w, event.h
                self.scale_factor = nWidth / SCREEN_WIDTH
                self.scaled_cell_size = int(CELL_SIZE * self.scale_factor)
                self.window = pygame.display.set_mode(
                    (nWidth, nHeight), pygame.RESIZABLE
                )
                
            self.selected_screen.handle_event(event)

        self.selected_screen.run()
        pygame.display.update()

    def is_running(self):
        return self.running

    def draw_board(self, left, top):
        board_width = BOARD_WIDTH * self.scaled_cell_size
        board_height = BOARD_HEIGHT * self.scaled_cell_size

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

        pygame.display.update()

    def draw_ship(self, lenght, left, top, color):
        pygame.draw.rect(
            self.window, color, pygame.Rect(left, top, lenght * CELL_SIZE, CELL_SIZE)
        )

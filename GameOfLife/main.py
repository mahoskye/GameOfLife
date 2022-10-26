import sys
import pygame
from board import Board

# Game Globals
SIZE = WIDTH, HEIGHT = 640, 480
CELL_SIZE = CELL_X, CELL_Y = 3, 3
SCREEN = pygame.display.set_mode(SIZE)
CELL_COLORS = {
    'color_alive': [74, 141, 104],
    'color_dead': [53, 39, 28]
}
CLOCK = pygame.time.Clock()
TICKS = 5
LAP = 0

pygame.display.set_caption("John Conway's Game of Life")

# Generate the game board
GAME_BOARD = Board(
    width=WIDTH,
    height=HEIGHT,
    cell_x=CELL_X,
    cell_y=CELL_Y,
    color_dead=CELL_COLORS.get('color_dead'),
    color_alive=CELL_COLORS.get('color_alive')
)


def start_loop():
    while 1:
        # Keep an eye out for user exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Clear the screen
        SCREEN.fill(CELL_COLORS['color_dead'])
        GAME_BOARD.update_state()

        for row in GAME_BOARD.BOARDS.get('current'):
            for cell in row:
                cell.check_state(GAME_BOARD.check_neighbors({'x': cell.POSITION.get('row'),
                                                             'y': cell.POSITION.get('column')}))

                pygame.draw.rect(SCREEN, *cell.build_rect())

        # Draw the board
        pygame.display.flip()
        CLOCK.tick(TICKS)


if __name__ == '__main__':
    start_loop()

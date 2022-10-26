import sys
import pygame
from board import Board

'''
# Rules

> From Wikipedia

The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in 
one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its 
eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, 
the following transitions occur:

1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These rules, which compare the behavior of the automaton to real life, can be condensed into the following:

1. Any live cell with two or three live neighbours survives.
2. Any dead cell with three live neighbours becomes a live cell.
3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.

The initial pattern constitutes the seed of the system. The first generation is created by applying the above rules 
simultaneously to every cell in the seed, live or dead; births and deaths occur simultaneously, and the discrete moment 
at which this happens is sometimes called a tick. Each generation is a pure function of the preceding one. The 
rules continue to be applied repeatedly to create further generations. 

## Translation

Board:
- 2d orthogonal grid (columns & rows)
- comprised of square cells
- cell contains 'life form' that is either alive or dead
- board will record two states
    - current generation
    - previous generation
- births and deaths occur simultaneously based in the previous generation

Cells:
- perfect squares
- status alive or dead
- initial state randomly selected

'''

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

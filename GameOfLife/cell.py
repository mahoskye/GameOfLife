import random


class Cell:
    def __init__(self, **kwargs):
        self.POSITION = {
            'row': kwargs.get('row_pos', 0),
            'column': kwargs.get('col_pos', 0)
        }

        self.CELL_SIZE = {
            'x': kwargs.get('cell_x', 5),
            'y': kwargs.get('cell_y', 5)
        }

        self.CELL_COLORS = {
            'alive': kwargs.get('cell_alive', [74, 141, 104]),
            'dead': kwargs.get('cell_dead', [53, 39, 28])
        }

        self.ALIVE = True if random.choice([0]*17 + [1]) else False
        self.COLOR = None
        self.update_color()

        return

    def build_rect(self):
        return [
            self.COLOR,
            [self.POSITION.get('row') * self.CELL_SIZE.get('x'),
             self.POSITION.get('column') * self.CELL_SIZE.get('y'),
             self.CELL_SIZE.get('x'),
             self.CELL_SIZE.get('y')]
        ]

    def check_state(self, living_neighbors):
        if self.ALIVE and living_neighbors in [2, 3]:
            self.ALIVE = True
        elif not self.ALIVE and living_neighbors == 3:
            self.ALIVE = True
        else:
            self.ALIVE = False

        self.update_color()

    def update_color(self):
        self.COLOR = self.CELL_COLORS.get('alive') if self.ALIVE else self.CELL_COLORS.get('dead')


if __name__ == '__main__':
    print("Cell")

from cell import Cell


class Board:

    def __init__(self, **kwargs):
        # Board size
        self.WINDOW_SIZE = {
            'width': kwargs.get('width', 640),
            'height': kwargs.get('height', 480)
        }

        # Cell size
        self.CELL_SIZE = {
            'x': kwargs.get('cell_x', 5),
            'y': kwargs.get('cell_y', 5)
        }

        # Board size
        self.BOARD_SIZE = {
            'rows': int(self.WINDOW_SIZE['width'] / self.CELL_SIZE['x']),
            'columns': int(self.WINDOW_SIZE['height'] / self.CELL_SIZE['y'])
        }

        # Cell coloration
        self.CELL_COLORS = {
            'color_alive': kwargs.get('color_alive', [74, 141, 104]),
            'color_dead': kwargs.get('color_dead', [53, 39, 28])
        }

        # Placeholder for board data
        self.BOARDS = {
            'current': self.create_board(),
            'previous': None
        }
        self.update_state()
        return

    def create_board(self):
        board = []
        # create row object and iterate
        for row_iter in range(self.BOARD_SIZE['rows']):
            row = []
            # create column object and iterate
            for col_iter in range(self.BOARD_SIZE['columns']):
                # generate a cell
                cell = Cell(
                    row_pos=row_iter,
                    col_pos=col_iter,
                    cell_x=self.CELL_SIZE['x'],
                    cell_y=self.CELL_SIZE['y'],
                    cell_alive=self.CELL_COLORS['color_alive'],
                    cell_dead=self.CELL_COLORS['color_dead']
                )
                row.append(cell)
            board.append(row)
        return board

    def update_state(self):
        self.BOARDS['previous'] = self.BOARDS.get('current')
        return None

    def check_neighbors(self, current_cell):
        living_neighbors = 0
        neighborhood = [
            [
                [current_cell.get('x')-1, current_cell.get('y')-1],
                [current_cell.get('x'),   current_cell.get('y')-1],
                [current_cell.get('x')+1, current_cell.get('y')-1]
            ],
            [
                [current_cell.get('x')-1, current_cell.get('y')],
                [current_cell.get('x')+1, current_cell.get('y')]
            ],
            [
                [current_cell.get('x')-1, current_cell.get('y')+1],
                [current_cell.get('x'),   current_cell.get('y')+1],
                [current_cell.get('x')+1, current_cell.get('y')+1]
            ]
        ]
        for street in neighborhood:
            for home in street:
                # Check if house is within bounds
                if 0 > home[0] or home[0] > self.BOARD_SIZE.get('rows')-1 \
                        or 0 > home[1] or home[1] > self.BOARD_SIZE.get('columns')-1:
                    continue
                if self.BOARDS.get('previous')[home[0]][home[1]].ALIVE:
                    living_neighbors += 1
        return living_neighbors

    def main(self):
        self.BOARDS['current'] = self.create_board()
        self.update_state()
        return self.check_neighbors({'x': 2, 'y': 3})


if __name__ == '__main__':
    b = Board()
    print("a: %s" % b.main())

ALIVE_CELL = 1
DEAD_CELL = 0


class GameOfLife:

    def __init__(self, state: list[list[int]]):
        """ Constructor

        Params:
            state (List[List[int]]): starting seed state
        """
        self.__state = state
        self.__generation = 0

    def run(self):
        """ Run the entire game of life until completion
        """
        print("Running Game of Life")
        self.__print_state()
        change_occured = True 
        while change_occured:
            next_state = []
            for row in range(len(self.__state)):
                next_row = []
                for column in range(len(self.__state[row])):
                    cell_type = self.__state[row][column]
                    live_count = self.__count_surrounding_alive_cells(row, column)
                    if cell_type == ALIVE_CELL:
                        next_cell = self.__alive_cell(live_count) 
                    else:
                        next_cell = self.__dead_cell(live_count) 
                    next_row.append(next_cell)
                next_state.append(next_row)
            self.__generation += 1
            change_occured = self.__has_changed(next_state)
            self.__state = next_state
            self.__print_state()

    def __has_changed(self, next_state) -> bool:
        """ Has there been a a change in cells from generation to generation
        """
        for row in range(len(self.__state)):
            for column in range(len(self.__state[0])):
                if next_state[row][column] != self.__state[row][column]:
                    return True
        print("Generation to generation no change, game ending")
        return False

    def __count_surrounding_alive_cells(self, row: int, column: int) -> int:
        """ Count live cells around a particular cell
        
        Params:
            row (int): row of state
            column (int): column of state
        Returns:
            (int) count of live cells
        """
        neighbor_cells = [
            [row - 1, column - 1],
            [row - 1, column],
            [row - 1, column + 1],
            [row, column - 1],
            [row, column + 1],
            [row + 1, column - 1],
            [row + 1, column],
            [row + 1, column + 1]
        ]
        live_count = 0
        for neighbor_cell in neighbor_cells:
            neighbor_row =  neighbor_cell[0]
            neighbor_column = neighbor_cell[1]
            # safe
            if (neighbor_row >= 0 and 
                neighbor_row < len(self.__state) and 
                neighbor_column >= 0 and 
                neighbor_column < len(self.__state[0]) and 
                self.__state[neighbor_row][neighbor_column] == ALIVE_CELL):
                    live_count += 1
        return live_count

    def __alive_cell(self, live_count: int) -> int:
        """ What to do for a live cell based on live surrounding neighbors

        Params:
            live_count (int): count of live cells surrounding an alive cell
        Returns:
            (int) alive cell either dead or live
        """
        if live_count >= 4 or live_count <= 1:
            return DEAD_CELL
        else:
            return ALIVE_CELL

    def __dead_cell(self, live_count: int) -> int:
        """ What to do for a dead cell based on live surrounding neighbors

        Params:
            live_count (int): count of live cells surrounding a dead cell
        Returns:
            (int) dead cell either dead or live
        """
        if live_count == 3:
            return ALIVE_CELL
        else:
            return DEAD_CELL

    def __print_state(self):
        """ Print the current state of the game
        """
        print("State at generation = {generation}"
              .format(generation=self.__generation))
        for row in self.__state:
            print(row)


if __name__ == '__main__':
    print("Demonstrating Test Pattern 1")
    game = GameOfLife(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
    )
    game.run()
    print("Demonstrating Test Pattern 2")
    game = GameOfLife(
        [
            [1, 1],
            [1, 0]
        ]
    )
    game.run()
    print("Demonstrating Glider pattern")
    game = GameOfLife(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
    )
    game.run()

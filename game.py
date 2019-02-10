class InvalidMoveError(Exception):
    def __init__(self, message):
        self.message = "An invalid move was attempted. Could not move {}".format(message)

class EightPuzzle:
    MOVES = {
        'u' : -3,
        'd' : 3,
        'l' : -1,
        'r' : 1
    }

    VALID_MOVES = [
        ['d', 'r'],
        ['d', 'l', 'r'],
        ['d', 'l'],
        ['u', 'd', 'r'],
        ['u', 'd', 'l', 'r'],
        ['u', 'd', 'l'],
        ['u', 'r'],
        ['u', 'l', 'r'],
        ['u', 'l']
    ]

    def __find_index_of_blank(self):
        return self.__board.index(9)

    def __init__(self, board):
        self.__board = [9 if x == 'E' else x for x in board]
        self.__blank_index = self.__find_index_of_blank()

    def is_valid_move(self, direction):
        return direction in self.VALID_MOVES[self.__blank_index]

    def move(self, direction):
        if self.is_valid_move(direction):
            self.__swap(self.MOVES[direction])
            return self.__board[:], self.__blank_index
        else:
            raise InvalidMoveError(direction)

    def set_gamestate(self, board, empty_pos=None):
        self.__board = [9 if x == 'E' else x for x in board]
        self.__blank_index = self.__find_index_of_blank() if empty_pos == None else empty_pos

    def is_solved(self):
        return all([a < b for a,b in zip(self.__board, self.__board[1:])])

    def get_available_moves(self):
        return [(k, self.peak(k)) for k in self.VALID_MOVES[self.__blank_index]]

    def peak(self, direction):
        future_state = self.move(direction)
        self.__swap(-self.MOVES[direction]) # reset board to its previous configuration
        return future_state


    def __swap(self, distance):
        old = self.__blank_index
        self.__blank_index += distance
        self.__board[old], self.__board[self.__blank_index] = self.__board[self.__blank_index], self.__board[old]

    # @staticmethod
    # def is_solvable(board):
    #     pass()

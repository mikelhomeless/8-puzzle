class InvalidMoveError(error):
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

    def __init__(self, board):
        self.__board = [9 if x == 'E' else x for x in board]
        self.__blank_index = __find_index_of_blank()

    def is_valid_move(self, direction):
        return direction in VALID_MOVES[self.__blank_index]

    def move(self, direction):
        if is_valid_move(direction):
            return __swap(self.__blank, MOVES[direction])
        else:
            raise InvalidMoveError(direction)

    def set_board(self, arr, empty_pos=None):
        self.__board = [9 if x == 'E' else x for x in board]
        self.__blank_index = __find_index_of_blank() if empty_pos == None else empty_pos

    def is_solution(self):
        return all([a < b for a,b in zip(self.__board, self.__board[1:])])

    def get_available_moves(self):
        return [k, peak(k) for k in MOVES if is_valid_move(k)]

    def peak(direction):
        future_board = move(direction)
        future_pos = self.__blank_index
        __swap(self.blank, -MOVES[direction])
        return future_board, future_pos

    def __find_index_of_blank(self):
        self.__board.index(9)

    def __swap(self, a, b):
        self.__board[a], self.__board[b] = self.__board[b], self.__board[a]
        return self.board

    @staticmethod
    def is_solvable(board):
        pass()

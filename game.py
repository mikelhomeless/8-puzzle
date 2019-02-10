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
        self.__board = board
        self.__blank_index = self.__find_index_of_blank()

    def is_valid_move(self, direction):
        return direction in self.VALID_MOVES[self.__blank_index]

    def move(self, direction):
        """move the blank space in the direction that was given
        direction -- char (See MOVES class variable)

        Returns a tuple of game state resulting from the move (board, blank_index)
        """
        if self.is_valid_move(direction):
            self.__swap(self.MOVES[direction])
            return self.__board[:], self.__blank_index
        else:
            raise InvalidMoveError(direction)

    def set_gamestate(self, board, empty_pos=None):
        """Manually set/change the state of the game
        board: array of integers, index is the integer's current position on the board
        empty_pos: location of the empty square. found automatically if not specified
        """
        self.__board = board
        self.__blank_index = self.__find_index_of_blank() if empty_pos == None else empty_pos

    def is_solved(self):
        return all([a < b for a,b in zip(self.__board, self.__board[1:])])

    def get_available_moves(self):
        """Return the set of moves that can be made in game's current state

        Returns a list of tuples of the following form (move: char, potential_game_state: tuple(potential_board, potential blank_index))
        """
        return [(k, self.peak(k)) for k in self.VALID_MOVES[self.__blank_index]]

    def peak(self, direction):
        """Test what the board would look like if a given move is made
        direction: char

        returns the potential board_state as a tuple (board, blank_index)
        """
        future_state = self.move(direction)
        self.__swap(-self.MOVES[direction]) # reset board to its previous configuration
        return future_state

    def __swap(self, distance):
        """Swap the index of the blank square with an index x indecies away
        distance: int - distance of away the square to swap with is
        """
        old = self.__blank_index
        self.__blank_index += distance
        self.__board[old], self.__board[self.__blank_index] = self.__board[self.__blank_index], self.__board[old]

    # @staticmethod
    # def is_solvable(board):
    #     pass()

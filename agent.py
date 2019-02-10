from heapq import *
class EightPuzzleAgent:
    def __init__(self, game):
        self.__game = game
        self.__queue = []
        self.__explored_states = set()

    def solve(self):
        """Obtain the optimal solution for EightPuzzle if it exists

        For each node/state explored, check if the current board is solved and return its history.
        If the puzzle is not yet solved, locate the next set of possible moves and push them into the
        priority queue (heap).

        If the queue is emptied, all possible states have been explored and no solution exists
        """
        self.queue_moves(self.__game.get_available_moves(), '')
        while self.__queue:
            priority, game_state, history = heappop(self.__queue)
            self.__game.set_gamestate(*game_state)
            if self.__game.is_solved():
                return history
            self.queue_moves(self.__game.get_available_moves(), history)

        return False

    def queue_moves(self, moves_list, move_history):
        """Push potential moves into the queue to be explored
        moves_list -- [(direction, (resulting_board_state, blank_position)),
                       (direction, (resulting_board_state, blank_position)), ... ]
        move_history -- string of all moves made on the board prior to the ones being added

        Go through every move in the provided list and check if the resulting board configuration has been seen before.
        If board is so far unique, add it to the set of explored states, then add the game state and move history to the queue
        """
        for item in moves_list:
            move, game_state = item
            if str(game_state[0]) not in self.__explored_states:
                self.__explored_states.add(str(game_state[0]))
                heappush(self.__queue, self.create_node(move, game_state, move_history))

    def manhattan_distance(self, arr):
        """
        Returns the manhattan distane of an entire array
        """
        return sum([self.mhd(index, num - 1) for index, num in enumerate(arr) if num != 9])

    def mhd(self, index, num):
        """Calculate the manhattan distance of an individual square
        index - the index the square is currently located in the array
        num - the value of the square (The position it should end up in the goal state)

        returns an integer
        """
        cur_row, cur_col = index // 3, index % 3
        goal_row, goal_col = num // 3, num % 3
        return abs(goal_row - cur_row) + abs(goal_col - cur_col)

    def create_node(self, move, game_state, history):
        """Create a node to be placed in the Priority Queue
        Returns a list with the following form [priority: int, state: tuple(board, empty tile position), history: str ]
        """
        # update the history to include the new move
        updated_history = history + move

        # Calculate priority based of manhattan_distance + moves made so far
        priority = len(history) + self.manhattan_distance(game_state[0])
        return priority, game_state, updated_history

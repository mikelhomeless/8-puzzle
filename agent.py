from heapq import *
class EightPuzzleAgent:
    def __init__(self, game):
        self.__game = game
        self.__queue = []
        self.__explored_states = set()

    def solve(self):
        self.queue_moves(self.__game.get_available_moves(), '')
        while self.__queue:
            search_node = heappop(self.__queue)
            self.__game.set_gamestate(*search_node[1])
            if self.__game.is_solved():
                return search_node[2]
            self.queue_moves(self.__game.get_available_moves(), search_node[2])
        return False

    # nodes are a list with the following form [priority, state - tuple(board, empt tile position), history - str ]
    def queue_moves(self, moves_list, move_history):
        for item in moves_list:
            move, game_state = item
            if str(game_state[0]) not in self.__explored_states:
                self.__explored_states.add(str(game_state[0]))
                updated_history = move_history + move
                priority = len(move_history) + self.manhattan_distance(game_state[0])
                heappush(self.__queue, (priority, game_state, updated_history))

    def manhattan_distance(self, arr):
        return sum([self.mhd(index, num - 1) for index, num in enumerate(arr)])

    def mhd(self, index, num):
    	cur_row, cur_col = index // 3, index % 3
    	goal_row, goal_col = num // 3, num % 3
    	return abs(goal_row - cur_row) + abs(goal_col - cur_col)

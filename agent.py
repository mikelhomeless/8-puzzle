from heapq import *
class EightPuzzleAgent:
    def __init__(self, game):
        self.__game = game
        self.__queue = []
        self.__explored_states = set()

    def solve(self):
        queue_moves(self.__game.get_available_moves(), '')
        while self.queue:
            search_node = heappop(self.queue)
            game.set_gamestate(*search_node[1])
            if game.is_solved():
                return search_node[2]
            queue_moves(self.__game.get_available_moves(), game_state[2])

    # nodes are a list with the following form [priority, state - tuple(board, empt tile position), history - str ]
    def queue_moves(self, moves_list, move_history):
        for item in moves_list:
            move, game_state = item
            if game_state[0] not in self.__explored_states:
                self.__explored_states.append(game_state[0])
                updated_history = move_history + move
                priority = len(move_history) + manhattan_distance(game_state[0])
                heappush(self.__queue, (priority, game_state, updated_history))

    def manhattan_distance(self, arr):
        return sum([abs((value - 1) - index) for index, value in enumerate(arr)])

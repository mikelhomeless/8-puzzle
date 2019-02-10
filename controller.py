from agent import EightPuzzleAgent
from game import EightPuzzle
from array import array

# input_array = list(map(int, input('Input the game board').split(',')))
# game = EightPuzzle(input_array)
# agent = EightPuzzleAgent(game)
#
# solution = agent.solve()
# if solution:
#     print(solution, len(solution))
# else:
#     print('No solution found. Nodes searched: {}'.format(solution[1]))

def puzzle_file(file):
    with open(file) as f:
        for x in range(int(f.readline())):
            yield get_board(f)
            f.readline()

def get_board(file):
    board = []
    for x in range(3):
        board.extend(file.readline().split())
    return board

input_file = 'prog1_input.txt'
for board in puzzle_file(input_file):
    board = [int(x) if x != 'E' else 9 for x in board ]
    game = EightPuzzle(array('B', board))
    agent = EightPuzzleAgent(game)

    solution = agent.solve()
    if solution:
        print(solution, 'for: ', board)
    else:
        print('No solution was found for {}'.format(board))

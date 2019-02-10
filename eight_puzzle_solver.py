from agent import EightPuzzleAgent
from game import EightPuzzle
import sys
import time

class InvalidInputError(Exception):
    def __init__(self):
        self.message = 'INVALID INPUT'

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

def validate_input(input_array):
    if not all([x in '12345678Ee' for x in input_array]) or len(input_array) != 9:
        raise InvalidInputError
    else:
        return input_array

def find_solution(board):
    board = [int(x) if x not in 'Ee' else 9 for x in board]
    game = EightPuzzle(board)
    agent = EightPuzzleAgent(game)
    start_time = time.time()
    solution = agent.solve()
    elapsed_time = time.time() - start_time
    if solution:
        if len(solution) == 0:
            print("Puzzle is already solved\n")
        else:
            print("Moves: {:.<31} steps: {:2d} solution found in: {:.3f}s\n".format(solution, len(solution), elapsed_time))
    else:
        print('No solution was found.\n')

# ______________________________________MAIN_______________________________________________
try:
    if len(sys.argv[1:]) == 0:
        board = validate_input(input("Please enter the board configuration separated by spaces: ").split())
        find_solution(board)
    elif len(sys.argv[1:]) == 1:
        start_time = time.time()
        for board in puzzle_file(sys.argv[1]):
            validate_input(board)
            print('Finding Solution for {}'.format(board))
            find_solution(board)
        print('{:.3f}s to solve all puzzles in file.'.format(time.time() - start_time))
    else:
        print('INVALID ARGUMENT')
except InvalidInputError:
    print('INVALID INPUT')

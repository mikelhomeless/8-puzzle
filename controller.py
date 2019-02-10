from agent import EightPuzzleAgent
from game import EightPuzzle

input_array = list(map(int, input('Input the game board').split(',')))
game = EightPuzzle(input_array)
agent = EightPuzzleAgent(game)

solution = agent.solve()
print(solution, len(solution))

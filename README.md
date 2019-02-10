# 8-puzzle

## Algorithm
This program uses the A* algorithm to search for the most optimal solution to a given
8-puzzle.

Heuristic: Manhattan Distance

Goal state: All tiles are in numerical order with the empty tile

NOTE: It _is_ possible for a given board to not have a solution (in fact, half of all possible board permutations don't have
      one). While the puzzles that _do_ have a solution will generally be solved in less than a second. Puzzles that don't have one must go through all moves (9!/2) and will therefore take much longer to complete (about 5 seconds for each unsolvable
      puzzle)
## How to use
There are two ways to use this program. The interface depends on the arguments given
when the program is called.

### No Arguments
```bash
python3 eight_puzzle_solver.py
```
When starting the program with no arguments, it will prompt the user to enter the
values of the puzzle separated by white space.

For example, the following 8-puzzle configuration
```
7 5 4
3 6 2
E 8 1
```

Would be typed in as:
```
7 5 4 3 6 2 E 8 1
```
with E (or e) denoting the blank tile

### One Argument
```bash
python3 eight_puzzle_solver.py file_path
```
Starting the program with one argument tells the program you want to load puzzles in from a file.
The argument should specify the full file path to the stored file so the program can find it (unless the file
  is in the same directory as the program)

The first line of each file specifies the number of puzzles located within it. Each puzzle should
be represented with each row on a new line with white space between tiles.

Example:
```
2
7 5 4
3 6 2
E 8 1

2 1 8
4 3 5
E 6 7
```

See the "example_puzzles.txt" file for examples
Solve them with
```bash
python3 eight_puzzle_solver.py example_puzzles.txt
```

## Reading output
If a solution for the puzzle provided exists, a list of moves will be printed to show the
steps found to solve.
- r = right
- l = left
- u = up
- d = down

Each step represents the direction the empty tile would need to be moved to reach the next state
Example:
We start with the following puzzle
```
7 5 4
3 6 2
E 8 1
```
Hypothetically, if the first move printed is 'r', then we move the empty tile right of its current location.
The resulting state follows
```
7 5 4
3 6 2
8 E 1
```

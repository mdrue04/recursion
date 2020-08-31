# Solving Sudoku and Hanoi: recursion vs. no recursion

## What?
This repository solves two puzzles using two different approaches.

The puzzles:
- The famous [Sudoku](https://de.wikipedia.org/wiki/Sudoku)
- and the lesser known [Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle.

The solutions:
- The first approach is using recursion.
- The second approach is replacing this recursive solution in a non-recursive manner.
---
## Why?
- On the one hand: Demonstrate the beauty of recursion, especially in the Hanoi example.
- On the other hand: Recursion is often not easily readable and has the tendency to be memory hungry if you do not pay close attention to what you are doing. In some development environments it might be even forbidden to use (e.g. embedded). This is why here we are replacing the recursive solutions with non-recursive ones.
---
## How?
### Sudoku
If you want to try out the solvers, just call them using python3. The input sudoku can be changed in sudoku/example_input/input_sudoku.txt and then just call

> python3 sudoku_solver.py

or

>python3 sudoku_solver_no_recursion.py

### Hanoi

Hanoi is even simpler to call, just use:

>python3 hanoi_solver.py -n 4

or

>python3 hanoi_solver_no_recursion.py -n 4

for a hanoi with the number of plates being 4 (default is 3).

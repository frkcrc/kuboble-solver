# Kuboble Solver

Solver for [Kuboble](https://kuboble.com/) puzzles.

Run the solver with:

> python3 solver.py <file>

`<file>` should be a file containing a level.

The file should contain the goal solution length on the first line, and then a representation of the board in the format specified below:
- `#` is a wall; the level does not need to be surrounded by walls.
- `.` marks an empty square.
- `A` marks a stone's starting square; each letter is a different stone.
- `a` marks a stone's target square; each letter is a different stone.

For example:

> 5
> #####  
> #BW.#  
> #...#  
> #wb.#  
> #####  

To run the tests, simply use:

> python3 -m unittest discover -v test

The `levels` directory contains a few levels for testing.
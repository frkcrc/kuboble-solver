# Kuboble Solver

Solver for [Kuboble](https://kuboble.com/) puzzles.

Run the solver with:

> python3 solver.py <file>

`<file>` should be a file containing a level, in the format specified below:
- `#` is a wall; the level should be surrounded by walls.
- `.` marks an empty square.
- `A` marks a stone's starting square; each letter is a different stone.
- `a` marks a stone's target square; each letter is a different stone.

For example:

> #####  
> #BW.#  
> #...#  
> #wb.#  
> #####  
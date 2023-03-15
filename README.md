# Kuboble Solver

Solver for [Kuboble](https://kuboble.com/) puzzles.

Run the solver with:

> python3 solver.py \<file>

`<file>` should be a file containing a level.

The file should contain, in order:
- The goal solution length on the first line;
- A list of `stone_name, start_row, start_col, target_row, target_col`.
- A representation of the board using `#` to mark walls and `.` to mark empty squares.
  - It's not necessary to surround everything with walls, but the coordinates used should match the representation (count the walls if using walls).

For example:

> `5`  
> `B,1,1,3,2`  
> `W,1,2,3,1`  
> `#####`   
> `#...#`  
> `#...#`  
> `#...#`  
> `#####`  

- This could be expressed without outer walls (but the coordinates should be adjusted to account for the missing row/col).



To run the tests, simply use:

> python3 -m unittest discover -v test

The `levels` directory contains a few levels for testing.
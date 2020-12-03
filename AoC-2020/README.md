# AoC-2020
Python solutions to Advent of Code 2020 puzzles.

---

## Puzzle Prompts
Puzzles can be found on the AoC [website](https://adventofcode.com/2020). Each day's puzzle can also be found in the `prompts` folder.

---

## Puzzle Comments 
Each puzzle I compete has:
1) A subjective 1-10 rating of how hard I thought it was
2) A few comments on how I approached it

These ratings and comments can be found below.

---

### Day 1 - 2/10
Very straightforward use of nested loops. ***I completed several days of AoC 2019 using C++ as a learning experience. Even after a single puzzle this year, it is clear that Python will be much easier to pick up.***

---

### Day 2 - 3/10
Basic string manipulation. Interesting that I was off by one for a while because there was not a newline character for the last line of the input. Since I stripped newlines for all the other lines, the last `d` of the last password was not counted and the password was erroneously marked as invalid. ***May be cheating, but I just added a newline to the last policy/password to resolve this.***
* Realized how useful the `zip` function is for looping over parrallel lists

---


### Day 3 - 1/10
Very straightforward use of modulo operator. Was a fun puzzle though. Second part was a good excersize in generalization.
* Python's list comprehensions made it easy to get the indices of each tree from the input lines.
* Using `reduce` from the `functool` library with a lambda function was very clean. Will probably try to use these more in future puzzles.
---

### Day 4 - ?/10

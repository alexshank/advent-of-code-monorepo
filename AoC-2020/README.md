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

### Day 4 - 5/10
A lot of work going through the input data and preparing it. I had more issues with off by one errors caused by the end of the input file. ***This time I cheated by adding TWO newlines to the end of the input file.***

I did not like the second part. It was a lot of redundent data validation work that wasn't really puzzle-like.
* List comprehensions useful again.
* First time I've used `list.extend()` rather than `list.append()`.
* During part 2, found a way to simplify field validation assuming no more than 8 fields ever present.
* First challenge where I needed test inputs and a debugger to fix my logic

---

### Day 5 - 3/10
An interesting take on binary search. Very straight forward puzzle. Off-by-one errors have been killing me!

---

### Day 6 - 2/10
First use of a `set` in any of these puzzles. I expected the second part to require you to analyze each person, so the first part isn't as optimized as it could be. (But premature optimization is death anyways!)

---

### Day 7 - 9/10
First puzzle that has been very difficult for me. Since I'm not great with trees, there was probably a more Pythonic/simpler way I could have solved Part I. My solution feels clumsy, and I doubt I was meant to implement tree search myself. Still, nice to have an excuse to write recursive functions and work with trees. Part II also threw me for a loop, because I ignored Bag counts for Part I, and the data doesn't exactly match a Tree datatype (there are duplicate branches that are children of multiple different parent branches)
* First absolutely neccessary use of a `Class` so far
* Recursive functions for searching for and counting items with my `Bag` tree
* I am currious how non-optimal my solution is. The complexity of the logic makes it hard to follow others' solutions and see how mine could be improved




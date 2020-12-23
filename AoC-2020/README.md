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

---

### Day 8 - 2/10
I have taken higher level computer architecture courses for my B.S. ECE, so I am very familiar with this puzzle's concept. Basically involved parsing the input data and manipulating a program counter.
* I think the OOP approach I took is very clean and simulates the gaming device nicely
* I used Python's `type hints` to specify that an `-> int` has to be returned by every executed instruction. I think this is only valuable if I run static code analysis on these puzzles though
* Made a very beginner pointer mistake while trying to make my code more readable with local variables. You can read `self.instructions[i]` into a local variable `instr`, but writing to `instr` will not change `self.instructions[i]`. This is because `self.instructions[i]` returns an immutable `string`. So, when `instr` is assigned a value, it is actually pointed to an entirely new address in memory with new immutable string data

---

### Day 9 - 1/10
I was completely convinced this would be one of those problems that looks straightforward, but takes much too long to compute. Turns out, it was just very straightforward!

---

### Day 10 - 5/10
Part I was very easy. Part II I couldn't solve myself, so I looked at [this](https://github.com/viliampucik/adventofcode/tree/master/2020) solution. I'm actually happy I had to check others' solutions, because they were much cleaner than what I would have hacked together.
* `defaultdict` can be very useful and I haven't really used them yet
* The `map` function is also a much cleaner way of modifying lists
* I really thought this would be a recursive problem, so I never saw the real way it should be approached

---

### Day 11 - 4/10
This has been my favorite puzzle so far. The first part shows how effective some simple optimizations can be. I went from a program that did not terminate in under a few minutes, to one that completes in about 5 seconds for Part II. Some optimizations to note:
1. I hardcoded the offset values needed for corner, side, and surrounded seats. This removed a lot of computations that were needed in my first, generalized solution
2. Any conditional I already knew the result of didn't get evaluated. For example, Part II originally checked if the offsets went out of bounds with a `while` loop. However, the first iteration is always `True`, so I moved the conditional check into the loop essentially creating a `do while`.
3. I am still trying to write "Pythonic" code, but I am unsure of the effects that list comprehensions, generators, and lambda functions have on execution times.

***I am realizing I won't finish this AoC by the 25th because I spent too much time optimizing, looking at others' solutions, and redoing things after I solve the puzzles.***

I was especially impressed by [this](https://github.com/metinsuloglu/AdventofCode20/blob/main/day11.py) solution, which uses vectorization (`numpy`) and 2D convolution (`scipy`) in a very clever way to determine the number of occupied seats around each seat. This is ***an entire*** solution to Part I.

```python
grid_converter = str.maketrans('.L#','012')
with open('inputs/day11.txt') as layout:
    grid = np.array([[int(x) for x in list(r.translate(grid_converter))]
                     for r in layout.read().splitlines()])

# Part 1
kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
curr_seats = np.copy(grid)
while True:
    prev_seats = np.copy(curr_seats)
    res = convolve(np.where(curr_seats == 2, 1, 0), kernel, mode='constant')
    curr_seats[(curr_seats == 1) & (res == 0)] = 2
    curr_seats[(curr_seats == 2) & (res >= 4)] = 1
    if (prev_seats == curr_seats).all(): break
                
part1 = np.count_nonzero(curr_seats == 2)
```
---

### Day 12 - 2/10
Part I was a very straighforward puzzle. Part II could be done a couple different ways.
* Using the `%` operator made implementing left and right turns very clean.
* Solution for Part II was also pretty straightforward, but I spent a lot of time trying to optimize calculating rotated points
    * I ended up using a wikipedia article on the [rotation matrix](https://en.wikipedia.org/wiki/Rotation_matrix)

---

### Day 13 - ?/10


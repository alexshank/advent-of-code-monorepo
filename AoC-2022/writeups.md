# AoC 2022 — Writeups

Per-day commentary on the 2022 solutions: what the puzzle actually asked for, and how I went at it.

Each day carries a subjective difficulty rating, the techniques it used, and a line worth remembering — usually pulled from my own comments or commit messages at the time. Same idea as the journals in the 2019 and 2020 READMEs, which 2022 never got despite being the only year I finished in full.

The collapsed reference block under each day quotes that day's code comments and commit messages, so I can review a day without reopening the source. Delete it once the day is written.

Keep the `## Day N — Title` headings and the `**Difficulty:**` / `**Tags:**` / `**Quote:**` lines as they are — see the note in the [repository README](../README.md#reuse) about a downstream consumer that parses them.

---

## Day 1 — Calorie Counting

- **Difficulty:** /10
- **Tags:** parsing
- **Quote:** My first Haskell program :) — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-1.py`

- L5: only work with ints
- L7: find indices with zeros
- L9: sum between all zeros
- L11: print sum of top 3

`day-1.hs`

- L8: create list of tuples containing sublist ranges (add boundary indices)
- L13: create list of sublists, then reduce each sublist to its sum
- L17: part 1
- L20: part 2 (sum the last 3 elements of sorted array)
- L23: ($) :: (a -> b) -> a -> b
- L24: the above is same as: print (sum (slice (sumCount - 3) sumCount (sort sums)))
- L26: take [1,2,3] and create [(1,2), (2,3)]
- L30: basically python's slicing functionality xs[from:to]
- L34: we need to convert to Int (sum undefined for String)

Commits

- Completed day 1.
- Messing with Haskell.
- Day 2 solution.
- My first Haskell program :)
- Completed day 6

</details>

---

## Day 2 — Rock Paper Scissors

- **Difficulty:** /10
- **Tags:** parsing, modular arithmetic
- **Quote:** Changed match to modulo operator. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-2.py`

- L6: part 1
- L18: part 2
- L22: choose rock, paper, scissors based on if we should lose, tie, or win

Commits

- Day 2 solution.
- Changed match to modulo operator.

</details>

---

## Day 3 — Rucksack Reorganization

- **Difficulty:** /10
- **Tags:** sets, parsing
- **Quote:** Completed day 3 puzzle. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-3.py`

- L9: part 1
- L17: part 2

Commits

- Completed day 3 puzzle.

</details>

---

## Day 4 — Camp Cleanup

- **Difficulty:** /10
- **Tags:** interval overlap, parsing
- **Quote:** take each line "19-24,45-67" -> [19, 24, 45, 67] — *day-4.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-4.py`

- L4: take each line "19-24,45-67" -> [19, 24, 45, 67]
- L9: part 1 (fully overlapped ranges)
- L16: part 2 (partially overlapped ranges)

Commits

- Completed day 4.

</details>

---

## Day 5 — Supply Stacks

- **Difficulty:** /10
- **Tags:** stacks, simulation
- **Quote:** we'll add the crates to the stacks in FILO order — *day-5.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-5.py`

- L5: returns list of lists (treat inner lists as stacks with append() and pop())
- L7: remove known spaces and brackets, convert 3 consecutive spaces into arbitrary "not present" symbol
- L15: we'll add the crates to the stacks in FILO order
- L24: move crates according to new or older functionality
- L36: split input into key parts
- L42: initialize stack data types for the literal crate stacks
- L45: parse list of movements into triples: (count, from_index, to_index)
- L51: part 1
- L55: part 2

Commits

- Completed day 5.
- Cleaning up.

</details>

---

## Day 6 — Tuning Trouble

- **Difficulty:** /10
- **Tags:** sliding window, sets
- **Quote:** recursion is no bueno for this (problem gets bigger) — *day-6.hs*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-6.hs`

- L7: let inputLine = take 1 lines
- L8: print (inputLine)
- L10: recursion is no bueno for this (problem gets bigger)

Commits

- Completed day 6
- Saving progress.

</details>

---

## Day 7 — No Space Left On Device

- **Difficulty:** /10
- **Tags:** tree structures, recursion, DFS
- **Quote:** higher-order function <==> function that takes functions as input — *day-7.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-7.py`

- L4: extend generic tree to store files on each node
- L8: application specific property
- L11: TODO this should be in the base class somehow, using Python's
- L12: TODO equivalent to generics
- L22: cannot use generic print because we want an application-specific property
- L30: example use case of the traversing higher-order function
- L31: higher-order function <==> function that takes functions as input
- L38: [(dir, size), ..., (dir, size)] where size >= threshold
- L54: switch dir command
- L59: dir listed
- L63: file size listed
- L68: seek to root node
- L73: show our nice file structure
- L76: part 1
- L82: part 2

Commits

- Completed day 7.
- Trying to modularize.

</details>

---

## Day 8 — Treetop Tree House

- **Difficulty:** /10
- **Tags:** grids, higher-order functions
- **Quote:** NOTE: Was trying to abuse higher-order functions. Obscure code below. — *day-8.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-8.py`

- L5: NOTE: Was trying to abuse higher-order functions. Obscure code below.
- L7: return trees to the left, right, above, below
- L12: how many trees you see before your view is blocked
- L20: part 1 - check if tree is visible from any direction (or, tree can see out of forest)
- L26: part 2 - score based on how many other trees are in a tree's view

Commits

- Completed day 8.
- Adding disclaimer.

</details>

---

## Day 9 — Rope Bridge

- **Difficulty:** /10
- **Tags:** simulation, grids
- **Quote:** always put the tail on the same col or row as head if it moves (handles diagonals) — *day-9.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-9.py`

- L19: always put the tail on the same col or row as head if it moves (handles diagonals)
- L30: part 1
- L34: part 2
- L48: always put the tail on the same col or row as head if it moves (handles diagonals)
- L52: can now have diagonals
- L65: print board
- L66: x_min = min([x[0] for x in rope])
- L67: x_max = max([x[0] for x in rope])
- L68: y_min = min([x[1] for x in rope])
- L69: y_max = max([x[1] for x in rope])
- L70: print('------')
- L71: print('After ' + direction + ' - ' + str(i + 1))
- L72: print('------')
- L73: for y in reversed(range(y_min, y_max + 1)):
- L74: 	for x in range(x_min, x_max+1):
- L75: # for y in reversed(range(-5, 20)):
- L76: # 	for x in range(-20, 20):
- L77: 		if (x,y) in rope:
- L78: 			# print('X', end='')
- L79: 			# print highest index in position
- L80: 			for m in reversed(range(len(rope))):
- L81: 				if rope[m] == (x,y):
- L82: 					if m == 9:
- L83: 						print('H', end='')
- L84: 					elif m == 0:
- L85: 						print('T', end='')
- L86: 					else:
- L87: 						print(str(len(rope) - 1 - m), end='')
- L88: 					break
- L89: 		else:
- L90: 			print('.', end='')
- L91: 	print()
- L93: part 2

Commits

- Saving progress.

</details>

---

## Day 10 — Cathode-Ray Tube

- **Difficulty:** /10
- **Tags:** simulation, CRT rendering
- **Quote:** Saving progress. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-10.py`

- L17: part 1
- L23: part 2

Commits

- Saving progress.

</details>

---

## Day 11 — Monkey in the Middle

- **Difficulty:** /10
- **Tags:** simulation, modular arithmetic, LCM
- **Quote:** least common multiple (LCM) of prime numbers (like we have) is just their product! — *day-11.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-11.py`

- L17: TODO could move so it isn't computed a ton
- L35: worry = worry // 3
- L46: get groups of lines between blank lines
- L48: TODO I've broken this now
- L60: part 2 (hint from Reddit: (a mod kn) mod n = a mod n for any positive integer k)
- L61: store a mod kn instead of a
- L62: so keep taking modulo of result after each divisor check
- L63: least common multiple (LCM) of prime numbers (like we have) is just their product!
- L64: k above is the lcm, or product of all the possible divisors
- L66: part 1 solution: 110220
- L67: part 2 solution: 19457438264

Commits

- Saving progress.

</details>

---

## Day 12 — Hill Climbing Algorithm

- **Difficulty:** /10
- **Tags:** BFS, grids, shortest path
- **Quote:** clever solution: You can just run BFS from the destination and have it terminate when it reaches ANY square that could have been a start square — *day-12.kt*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-12.kt`

- L5: get input grid and dimensions
- L10: pad around grid so we can ignore edge conditions
- L18: part 1 (we know !! is safe here)
- L21: TODO clever solution: You can just run BFS from the destination and have it terminate
- L22: TODO when it reaches ANY square that could have been a start square
- L23: part 2
- L36: returns a shortest path to the desired coord, or null if no path exists
- L59: data classes give us proper equality checks for free

Commits

- Saving progress.
- Refactored day 12.
- Completed day 12 in Kotlin.
- Starting day 24.

</details>

---

## Day 13 — Distress Signal

- **Difficulty:** /10
- **Tags:** recursion, parsing, custom sort
- **Quote:** Completed day 13. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-13.py`

- L4: remove enclosing []
- L7: empty list base case
- L10: TODO alex not needed?
- L14: just ints base case
- L94: part 1 (answer: 5717)
- L97: part 2 (answer: 25935)

Commits

- Completed day 13.

</details>

---

## Day 14 — Regolith Reservoir

- **Difficulty:** /10
- **Tags:** simulation, complex-number grids, sets
- **Quote:** Completed day 14. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-14.py`

- L53: should never hit in part 2
- L54: if location.imag > y_max:
- L55: 	return None
- L57: elif
- L60: TODO don't think we need edge conditions
- L61: elif location.real - 1 >= x_min and location - 1 + 1j not in rock_map.keys():
- L64: elif location.real + 1 <= x_max and location + 1 + 1j not in rock_map.keys():
- L68: part 2 edge case, we can't move at all from start location
- L77: part 1 (answer: 901)
- L78: count = 0
- L79: while (location := get_next_location()) != None:
- L80: 	rock_map[location] = 'O'
- L81: 	count += 1
- L82: print_rock_map()
- L83: print(count)
- L86: part 2 (answer: 24589)

Commits

- Completed day 14.

</details>

---

## Day 15 — Beacon Exclusion Zone

- **Difficulty:** /10
- **Tags:** interval merging, geometry
- **Quote:** If a row intersects a circle (defined by the sensor and beacon pair), then there will be two x coordinates defined by the intersection. — *day-15.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-15.py`

- L13: If a row intersects a circle (defined by the sensor and beacon pair),
- L14: then there will be two x coordinates defined by the intersection.
- L15: All x coordinates between these intersections cannot contain beacons
- L34: take x pairs (1, 5), (3, 13) --> (1, 13)
- L64: part 1 (answer: 5112034)
- L69: part 2 (answer: 13172087230812)

Commits

- Completed day 15.

</details>

---

## Day 16 — Proboscidea Volcanium

- **Difficulty:** /10
- **Tags:** Dijkstra, graph contraction, DFS, memoization
- **Quote:** No!! Greedy doesn't work. What about top N candidates? — *handwritten notes*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-16.py`

- L9: TODO could probably move all the standard algorithms I implementationed for AoC to a helper library
- L11: find adjacent, unvisted vertices
- L22: get all vertices adjacent to given vertex
- L33: returns dict of key: destination, value: path to destination
- L45: return None if there isn't a path from source to destination
- L52: compute shortest paths and shortest distances to every vertex in graph
- L59: algorithm must consider all vertices to complete
- L61: break early if there's no reachable, unactivated vertices
- L66: visit new vertex, mark it as the prior of its unvisted, adjacent vertices
- L73: note: walrus operator makes this more concise. it's both a statement and an expression
- L111: TODO likely don't need so much state passed around
- L112: TODO something like DFS of the state tree would likely be MUCH faster. tree structure may need to be modified for that, though
- L143: child states from the elephant taking action
- L154: child states from the human taking action
- L168: TODO should attempt some caching, this seems to be on the right track. DFS possibly on our tree of states? Actually contract the graph?
- L169: TODO don't actually store the paths between each node, just the distances?
- L172: TODO this isn't correctly caching
- L178: root node / state is the only one that doesn't contain a valve opening action
- L195: result = max([current_score + child_state.get_max_score() for child_state in child_states])
- L196: score_cache[cache_key] = result
- L198: return result
- L202: TODO move this out of global space
- L208: parse graph information from input
- L221: create vertex and edge sets
- L229: compute shortest path between every possible vertex pair
- L232: compute all the possible movements between nonzero pressure valves at all timesteps
- L233: this lookup object saves many, many recursive list creations
- L244: get every possible order we could release the valves in by ourselves
- L248: part 1: answer is 1915. no caching necessary
- L251: get every possible order we could release the valves in with elephant's help
- L256: part 2: answer is 2772. took ~8 minutes to run with caching

Commits

- Fixing file structure.
- Parsing day 16 input.
- Implemented Dijkstra's Algorithm for shortest paths.
- Saving progress.
- Completed day 16 part 1.
- Getting correct solution on test input. Real input is much too slow.
- Saving progress on a different OOP approach.
- Completed day 16 part 2 (slowly).

</details>

---

## Day 17 — Pyroclastic Flow

- **Difficulty:** /10
- **Tags:** simulation, cycle detection, complex-number grids
- **Quote:** LCM doesn't work obstensibly. Leaving notes for later. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-17.py`

- L9: part 1: 2022
- L10: part 2: 1_000_000_000_000
- L65: frozenset is an immutable built-in, meaning it can be hashed and added to a set
- L74: parse rock definitions
- L75: a rock's location is represented by a set of complex coordinates
- L76: a rock definition is a set of complex coordinates defined from its bottom-left corner
- L87: parse cycular wind movements
- L119: blown by wind
- L123: check wall conditions
- L128: move down 1
- L131: check stopping conditions
- L137: TODO could probably get last diff in a cleaner/faster way
- L154: part 1 (answer: 3127)
- L155: part 2 (answer: 1542941176480)

Commits

- Working copy. Slow though.
- Working copy. Slow though.
- Adding TODO comment.
- Adding TODO comment.
- Cleaning up. Still trying to figure out way to detect pattern.
- LCM doesn't work obstensibly. Leaving notes for later.
- Found a way to catch when the pattern starts :)
- Very close...
- Completed day 17.

</details>

---

## Day 18 — Boiling Boulders

- **Difficulty:** /10
- **Tags:** BFS, 3D grids, flood fill
- **Quote:** bfs "expands" the outside air around the lava blob — *day-18.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-18.py`

- L14: bfs "expands" the outside air around the lava blob
- L32: comprehensive set is inefficient, but allows us to ignore edge conditions
- L41: part 1 (answer: 4364)
- L44: part 2 (answer: 2508)

Commits

- Working on days 18 and 19.
- Completed day 18.

</details>

---

## Day 19 — Not Enough Minerals

- **Difficulty:** /10
- **Tags:** DFS, heaps, search pruning, memoization
- **Quote:** I needed A LOT of hints and references from the Advent of Code Reddit threads. I would not have solved this without them. — *README*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-19.py`

- L9: constants
- L14: TOTAL_TIME = 24
- L18: the triangular numbers for getting geode upper bounds
- L26: (-geodes, -obsidian, -clay, remaining_time)
- L53: determine the next time that a robot could be built based on current robots and resources
- L56: if already have the resources to build robot, return early
- L60: check if we have existing robots that can eventually mine us the resources for the new robot
- L66: TODO likely a cleaner, integer way of doing this without ceiling function
- L67: compute how many time steps it will take to acquire enough resources to build the new robot
- L79: find the maximum number of each robot we would ever want
- L80: if we can only spend X ore per turn, we would never want X + 1 ore robots
- L81: this is the main thing that reduces our search space
- L90: runs logic via DFS queue
- L92: help caching states by limiting max number of robots
- L95: help caching states by limiting max number of resources
- L98: tracks most geodes found at each time step
- L99: gets compared to the max number of possible remaining geodes to reduce search space
- L100: if most geodes at time t is already more than theoretical max, skip searching that branch
- L101: our heap hopefully surfaces good candidates first, making this a very useful pruning check
- L104: initialize resources and robots
- L109: actual BFS queue logic (and heap for priority queueing)
- L115: grab next state off queue
- L118: continue immediately if we've already seen this state
- L124: exit early if end of simulation
- L127: save best results up to this point and at this specific time (for caching)
- L134: compute absolute upper bound of geodes we could get from this current state
- L135: this assumes you could build one new geode robot at every remaining time step
- L136: trim this branch off the search, if it clearly will not beat the current best
- L142: possible robots that could be built and when
- L155: if impossible to build the robot type at all or before time's up, continue
- L156: if robot built at time 24, it doesn't contribute any mining
- L160: we could build at least one robot type later by waiting, so we should add a new state where we simply wait this turn
- L163: if the child offset is 0, build immediately and go to next state
- L165: update resources
- L169: clamp resources so that we don't track inconsequential states
- L175: add new robot to counts
- L179: add new state to BFS queue
- L183: we build the robot at a future time, so just collect resources and queue next state
- L185: add resources, new robot isn't available to mine resources until end of this step
- L189: clamp resources so that we don't track inconsequential states
- L195: add new state to BFS queue
- L199: collect resources from this turn
- L202: queue the state where we build nothing, but only if we can evenutally build SOMETHING by waiting
- L204: clamp resources so that we don't track inconsequential states
- L210: add new state to BFS queue
- L214: save best results up to this point and at this specific time (for caching)
- L221: returns array of dictionaries like blueprint['ore']['obsidian'] = 5
- L222: i.e., this blueprint specifies that an ore robot needs 5 obsidian
- L247: get max geodes that the blueprint could produce from simulation start
- L250: compute relevant quality metric
- L251: result = (i + 1) * max_geodes # part 1
- L254: view cache efficacy
- L257: measure elapsed time for this blueprint
- L270: put blueprints in global namespace so we can cache methods
- L275: sum up all the results
- L277: answer = sum(results)
- L280: part 1 (answer: 1127)
- L281: part 2: 21, 27, 37 => 20979 (got this hint by using someone else's solution on my input...)
- L282: part 2: 21, 27, 38 => 21546 (turns out their solution wasn't exactly correct for my input though!)
- L283: part 2 (answer: 21546)
- L286: print overall run time

Commits

- Working on days 18 and 19.
- Parsed input.
- Saving progress. In broken state, running too slowly.
- Saving before attempting to simplify.
- Very slow solution working for test input. Need to reduce problem space in some way.
- Attempting to reduce problem space. Much faster now, answer is off though.
- Adding notes for each day. Might add to personal website.
- Saving progress again.
- Running much faster after move to tuples. Answer off though.
- Results on test input now instantaneous, but off.
- Continuing debugging efforts.
- Chagning from time left to simply current minute.
- More debugging and simplifications.
- Picking back up. Improving console output formatting.
- Example inputs now working correctly.
- Updating caching strategy.
- Working on profiling of slow logic.
- Trying data class approach, but is slower.
- Simplified / optimized tuple helper methods.
- Multiprocessing attempt.
- Finished part 1.
- Trying to put more constraints on search space.
- Running quickly enough, but still finding non-optimal solution.
- Narrowing down the flaw in non-optimal solution.
- Setting up rework again for build nothing considerations.
- Still running too slowly.
- Still running slowly.
- Converting to BFS approach, part 1 answer now incorrect, but promising.
- Getting very close...
- Part 1 working again.
- Part 1 save point.
- Max resources pre-computed.
- Clean up.
- Working much faster with resource clamps. Part 1 no longer needs parallel execution.
- Part 1 working quickly and correctly. Part 2 fast but answer is incorrect.
- Will have to start debugging why part 2 answer is wrong.
- Marginal speed up.
- Need to get the example input working faster for part 1.
- Still so slow for part 1.
- Completed day 19.

</details>

---

## Day 20 — Grove Positioning System

- **Difficulty:** /10
- **Tags:** circular lists
- **Quote:** I still do not intuitively understand "moving the number forward/backward." P.S. See git history for many confused attempts! — *day-20.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-20.py`

- L3: Note: I still do not intuitively understand "moving the number forward/backward."
- L4: The solution below is based on a Reddit Advent of Code solution I read,
- L5: but I would not consider this behavior what the problem describes.
- L7: Accepting defeat on this one since I can't get any further explanation of the prompt.
- L8: I feel good about the coding concepts this was driving at though.
- L10: P.S. See git history for many confused attempts!
- L16: i = the new index of a number after being mixed
- L17: v = the original index of the number
- L23: This is the very unintuitive behavior imo:
- L24: (1) We wrap the list while the element is removed?
- L25: (2) Moving an element to position zero sends it to the back?
- L27: Note: len(indices) is len(numbers) - 1 during this call
- L34: part 1 (answer: 14526)
- L42: part 2 (answer: )

Commits

- Starting day 20.
- saving progress. Can't find bug.
- Example case working. Multiple wraps causing issues?
- Simplifying logic. Still not getting challenge input correct?
- Found issue, still need to implement fix.
- Completed day 20 (with help).

</details>

---

## Day 21 — Monkey Math

- **Difficulty:** /10
- **Tags:** tree structures, symbolic solve, recursion
- **Quote:** we build an expression like below and solve it with a library — *day-21.py*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-21.py`

- L45: print the math expression represented by the tree structure
- L61: initialize dictionary of tree nodes
- L64: connect the tree nodes to form the full tree
- L74: part 1 (answer: 21208142603224)
- L77: part 2 (answer: 3882224466191)
- L88: we build an expression like below and solve it with a library
- L89: Eq((5*(3-(4*X))), 150)

Commits

- Completed day 21.

</details>

---

## Day 22 — Monkey Map

- **Difficulty:** /10
- **Tags:** complex-number grids, cube folding, simulation, memoization
- **Quote:** Digressing, will come back with visualization. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-22.py`

- L37: if we go from side k to side j, find out what transition we need to make
- L39: TODO could use partial function application here :)
- L58: special cases?
- L63: keep track of sides you transition to going out of current square left, up, right, or down
- L86: TODO could cache this computation
- L117: no transformation needed
- L157: # view window of y's
- L158: min_y = max(min_y, int(current_location.imag) - 20)
- L159: max_y = min(max_y, int(current_location.imag) + 20)
- L180: TODO can we re-use common "board looking input" logic?
- L190: parse instructions in to ['R42', 'L43', ...]
- L200: TODO move into function (used in compute... function above)
- L206: TODO also maintain relative position
- L229: TODO may need to get back the new direction index and current side
- L239: print_board(display_board, current_abs_location, arrows[direction_index % 4], current_side)
- L241: if counter == 600:
- L242: 	break
- L245: TODO use the nice printing function for an animation
- L246: TODO make solution generic so both part 1 and part 2 can be solved
- L248: part 1 (answer: 165094)
- L249: part 2 (answer: 95316)

Commits

- Starting day 22.
- Incorrect implementation, need to turn not UDLR.
- Example working...
- Digressing, will come back with visualization.
- Fixed part 1 calculation :)
- Preparing for part 2.
- Saving part 1 before I change a bunch for part 2.
- Saving progress. Printing board to see issues.
- Saving progress on janky version.
- Completed day 22.

</details>

---

## Day 23 — Unstable Diffusion

- **Difficulty:** /10
- **Tags:** simulation, complex-number grids, sets
- **Quote:** Completed day 23. — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-23.py`

- L30: TODO can we re-use common "board looking input" logic?
- L45: key is square to move to, value is list of elves wanting to move there
- L47: for round_num in range(10):
- L50: for every elf square
- L53: TODO clean up. Check every direction
- L62: for every mask
- L77: part 2 (answer: 925)
- L83: part 1 (answer: 3871)
- L84: print_board(elves)

Commits

- Completed day 23.
- Starting day 24.

</details>

---

## Day 24 — Blizzard Basin

- **Difficulty:** /10
- **Tags:** BFS, cycle detection, complex-number grids, memoization
- **Quote:** Massive speedup by caching blizzard movements :D — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-24.py`

- L18: TODO could speed up by updating blizzards in place?
- L41: TODO this is likely slow
- L46: TODO the potential_square == traveler just allows the elf to stay in the start position
- L53: our nodes / states are a given position at a given time
- L78: load data into a data structure
- L95: should be the >, <, v, and ^ cases
- L99: the width and height of the board without walls
- L106: part 1 (answer: 308)
- L109: part 2 (answer: 908)

Commits

- Setting up day 24. Should automate this for next year.
- Starting day 24.
- Test input working.
- Still running too slowly.
- Massive speedup by caching blizzard movements :D
- Completed day 24 part 2.
- Adding day 24 prompt.

</details>

---

## Day 25 — Full of Hot Air

- **Difficulty:** /10
- **Tags:** base conversion, greedy
- **Quote:** Still trying to find pattern... — *commit*

TODO

<details><summary>Reference — my comments and commits for this day</summary>


`day-25.py`

- L35: total = 36067808580527
- L45: part 1 (answer: 2-212-2---=00-1--102)
- L49: at most 2 -> =, or 4 decrements

Commits

- Working on hacky version.
- Still trying to find pattern...
- Completed day 25 part 1.

</details>

---

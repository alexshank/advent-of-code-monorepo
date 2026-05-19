# AoC-2019

Solutions to Advent of Code 2019 (only days 1–6). Written in C++ to get familiar with the language's syntax and standard library. Migrated here from `misc-languages/misc-cpp/`.

## Layout

```
AoC-2019/
├── day-01/ … day-06/   # one folder per day: solution.cpp, input.txt, README.md (prompt)
└── solution-template/  # starter scaffolding used when beginning a new day
```

Each `README.md` inside a `day-XX/` folder contains the puzzle prompt for both parts and the recorded answers.

## Build / run

The originals were built with MSVC (Developer Command Prompt for VS 2017). Any modern C++ compiler works. For example, from any day's directory:

```shell
g++ -std=c++17 solution.cpp -o solution && ./solution
```

Each solution reads `input.txt` from the current working directory, so run commands from inside the day's folder.

## Journal

1. Getting used to C++ syntax. Nice to see a good use case for recursion (seems rare in practice).
2. I recently simulated a RISC computer in Register Transfer Notation for my Computer Architecture course at Ohio State. This problem is very similiar, so using good C++ practices was my mine focus.
3. I originally solved this problem with brute force, but the solution was slow. Implementing unordered sets in C++ is not trivial and I didn't want to develop a hash function for the line segments, so I calculated line segment intersections. Still think the logic could be cleaner somehow...
4. At first I tried to overcomplicate this because I was worried about the brute force issue I had with Day 3. Turns out you can just check every number's validity to solve this challenge, which is relatively easy.
5. Ran into many off-by-1 indexing errors here, but implemented the additional instructions. Learned that the `array[]` operator does not throw out of bounds exception, so `array.at()` must be used if you risk going out of array bounds.
6. C++ does not provide a tree datatype in the STL library, so I implemented a basic tree datatype with string and set datatypes. I would try the Boost library, but I want to complete these challenges with "pure" C++.

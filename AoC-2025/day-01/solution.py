"""
Solutions to Advent of Code 2025 - Day 1
"""


def solution_01():
    lines = None
    with open("./day-01/input.txt", "r") as input_file:
        lines = input_file.readlines()
    lines = [l.strip("\n") for l in lines if l.strip("\n")]

    nums = [int(l[1:]) if l[0] == "R" else -int(l[1:]) for l in lines]

    sums = [50 + nums[0]]
    for a in nums[1:]:
        sums.append(sums[-1] + a)

    return len(list(s for s in sums if s % 100 == 0))


"""
Was stumped by part 2. Had to find a solution on Reddit. I understood it enough to tweak it to my style.
"""


def solution_02():
    lines = None
    with open("./day-01/input.txt", "r") as input_file:
        lines = input_file.readlines()
    lines = [l.strip("\n") for l in lines if l.strip("\n")]

    rotations = 0
    dir = "R"
    cur_pos = 50
    for line in lines:
        new_dir = line[0] == "L"
        num = int(line[1:])

        # flip clock entirely, so everything is a right turn without edge cases
        if dir != new_dir:
            # need the modulo here in case cur_pos is 0 and leads to 100 - 0 = 100
            cur_pos = (100 - cur_pos) % 100
            dir = new_dir

        new_pos = cur_pos + num
        rotations += new_pos // 100
        cur_pos = new_pos % 100

    return rotations


if __name__ == "__main__":
    print()
    print("-------- Day 1 --------")
    print(f"Part 1: {solution_01()}")
    print(f"Part 2: {solution_02()}")
    print()

def solution_01():
    lines = None
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
    lines = [l.strip("\n") for l in lines if l.strip("\n")]

    nums = [int(l[1:]) if l[0] == "R" else -int(l[1:]) for l in lines]

    sums = [50 + nums[0]]
    for a in nums[1:]:
        sums.append(sums[-1] + a)

    return len(list(s for s in sums if s % 100 == 0))


"""
Was stumped by part 2. Had to find a solution on Reddit.
"""


def solution_02():
    lines = None
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
    lines = [l.strip("\n") for l in lines if l.strip("\n")]

    rotations = 0
    dir = "R"
    # at start of each loop, cur_pos could be much larger than 100
    cur_pos = 50
    for line in lines:
        new_dir = line[0] == "L"
        num = int(line[1:])

        # flip clock entirely, so everything is a right turn without edge cases
        if dir != new_dir:
            cur_pos = (
                100 - cur_pos
            )  # e.g., 100 - 813 = 713. Then, 713 % 100 = 13 is new position
            dir = new_dir

        # note that cur_pos here can be > 100, since num can be any positive int
        cur_pos = (cur_pos % 100) + num
        rotations += cur_pos // 100

    return rotations


if __name__ == "__main__":
    print(f"{solution_01()=}")
    print("-----")
    print(f"{solution_02()=}")

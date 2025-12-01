def solution():
    lines = None
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
    lines = [l.strip("\n") for l in lines if l.strip("\n")]

    nums = [int(l[1:]) if l[0] == "R" else -int(l[1:]) for l in lines]

    sums = [50 + nums[0]]
    for a in nums[1:]:
        sums.append(sums[-1] + a)

    return len(list(s for s in sums if s % 100 == 0))


if __name__ == "__main__":
    print(solution())

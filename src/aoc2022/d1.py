#!/usr/bin/env python3

from aoc2022 import DATAPATH

with open(DATAPATH.joinpath("input_d1.txt")) as f:
    lines = f.read().splitlines()

elves: list[int] = []
total: int = 0

for line in lines:
    if line:
        total += int(line)
    else:
        elves.append(total)
        total = 0

print(max(elves))
print(sum(sorted(elves)[-3:]))

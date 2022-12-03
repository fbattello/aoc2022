#!/usr/bin/env python3

from string import ascii_letters
from aoc2022 import DATAPATH

with open(DATAPATH.joinpath("input_d3.txt")) as f:
    rucksacks = f.read().splitlines()

items: list[str] = []
for r in rucksacks:
    size = len(r) // 2
    c1, c2 = r[:size], r[size:]
    items.append(set([x for x in c1 if x in c2]).pop())

priority = lambda x: ascii_letters.index(x) + 1

print(sum(priority(x) for x in items))

badges: list[str] = []
n = len(rucksacks) // 3
for i in range(n):
    r1, r2, r3 = rucksacks[i*3:i*3+3]
    badges.append(set(r1).intersection(set(r2), set(r3)).pop())

print(sum(priority(x) for x in badges))
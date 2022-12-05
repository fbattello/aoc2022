#!/usr/bin/env python3

import re
import copy
from aoc2022 import DATAPATH

pattern_stacks = re.compile(r"([A-Z]{1})")
pattern_moves = re.compile(r"move (\d+) from (\d+) to (\d+)")

stacks_orig = [[] for _ in range(9)]
moves = []

with open(DATAPATH.joinpath("input_d5.txt")) as f:
    lines = f.read().splitlines()

for line in lines[:8]:
    for crate in pattern_stacks.finditer(line):
        stacks_orig[crate.span()[0]//4].append(crate[1])

for i in range(9):
    stacks_orig[i].reverse()

# Puzzle #1

stacks = copy.deepcopy(stacks_orig)

for line in lines[10:]:
    m = pattern_moves.match(line)
    moves.append(tuple(int(m[i+1]) for i in range(3)))

def move(qty: int, src: int, dst: int):
    for _ in range(qty):
        crate = stacks[src-1].pop()
        stacks[dst-1].append(crate)

for m in moves:
    move(*m)

print("".join([x[-1] for x in stacks]))

# Puzzle #2

stacks = copy.deepcopy(stacks_orig)

def move(qty: int, src: int, dst: int):
    stacks[src-1], crates = stacks[src-1][:-qty], stacks[src-1][-qty:]
    stacks[dst-1].extend(crates)

for m in moves:
    move(*m)

print("".join([x[-1] for x in stacks]))

#!/usr/bin/env python3

from aoc2022 import DATAPATH

parse = lambda line: tuple((tuple(map(int, x.split("-"))) for x in line.split(",")))

with open(DATAPATH.joinpath("input_d4.txt")) as f:
    pairs = [parse(x) for x in f.read().splitlines()]

pairs_sorted = [sorted(x, key=lambda x: x[1]-x[0]) for x in pairs]
pairs_fullycontain = [(p1, p2) for p1, p2 in pairs_sorted if p1[0]>=p2[0] and p1[1]<=p2[1]]
print(len(pairs_fullycontain))

pairs_sorted = [sorted(x) for x in pairs]
pairs_overlap = [(p1, p2) for p1, p2 in pairs_sorted if p1[1]>=p2[0]]
print(len(pairs_overlap))

#!/usr/bin/env python3

from aoc2022 import DATAPATH

with open(DATAPATH.joinpath("input_d2.txt")) as f:
    ops = [x.replace(" ", "") for x in f.read().splitlines()]

# pre-computed scores
scores = {"AX": 4, "AY": 8, "AZ": 3, "BX": 1, "BY": 5, "BZ": 9, "CX": 7, "CY": 2, "CZ": 6}

def rpsround1(op: str) -> int:
    """op stands for Opponent, Player."""
    return scores[op]

loose_map = {"A": "Z", "B": "X", "C": "Y"}
win_map = {"A": "Y", "B": "Z", "C": "X"}

def rpsround2(op: str) -> int:
    """Here p is not the player shape but the player strategy."""
    o, strategy = op
    # compute the player shape
    if strategy == "Y":  # draw
        p = chr(ord(o)+23)  # old-school ascii trick
    elif strategy == "X":  # loose
        p = loose_map[o]
    else:  # win
        p = win_map[o]
    return rpsround1(o+p)

print(sum((rpsround1(op) for op in ops)))
print(sum((rpsround2(op) for op in ops)))

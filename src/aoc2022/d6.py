#!/usr/bin/env python3

from dataclasses import dataclass
from aoc2022 import DATAPATH

with open(DATAPATH.joinpath("input_d6.txt")) as f:
    buffer = f.read().rstrip("\n")

# Puzzle 1

@dataclass
class StartOfPacketMarker:
    marker: str = "...."
    def __iadd__(self, b: str):
        self.marker = b + self.marker[:-1]
        return self
    def __bool__(self):
        return "." not in self.marker and len(set(self.marker)) == 4

marker = StartOfPacketMarker()
for i, b in enumerate(buffer, 1):
    marker += b
    if marker:
        break

print(i)

# Puzzle 2

@dataclass
class StartOfMessageMarker:
    marker: str = "." * 14
    def __iadd__(self, b: str):
        self.marker = b + self.marker[:-1]
        return self
    def __bool__(self):
        return "." not in self.marker and len(set(self.marker)) == 14

marker = StartOfMessageMarker()
for i, b in enumerate(buffer, 1):
    marker += b
    if marker:
        break

print(i)

#!/usr/bin/env python3

from __future__ import annotations
from aoc2022 import DATAPATH

class File:
    def __init__(self, name: str, size: int = 0):
        self.name = name
        self._size = size

    def size(self):
        return self._size

class Directory(File):
    def __init__(self, name: str, parent: Directory = None):
        super().__init__(name)
        self.parent = parent
        self.files: dict[str, File] = {}
        self.directories: dict[str, Directory] = {}
        
    def add_file(self, file: File):
        self.files[file.name] = file

    def add_dir(self, directory: Directory):
        self.directories[directory.name] = directory

    def relative(self, dirname: str):
        if dirname == "..":
            return self.parent
        else:
            return self.directories[dirname]

    def size(self):
        return sum([f.size() for f in self.files.values()]) + sum([d.size() for d in self.directories.values()])

class Parser:
    def __init__(self, stdout = None, verbose = False):
        self.cwd = self.root = Directory("/", parent=None)
        self.verbose = verbose
        if not stdout:
            with open(DATAPATH.joinpath("input_d7.txt")) as f:
                stdout = f.read()
        self.lines = stdout.splitlines()

    def parse_line(self, line: str):
        tokens = line.split()
        if tokens[0] == "$":  # command
            cmd = tokens[1]
            if self.verbose:
                print(f"found command : {' '.join(tokens[1:])}")
            if cmd != "cd":
                return
            value = tokens[2]
            if value != "/":
                newcwd = self.cwd.relative(value)
                if self.verbose:
                    print(f'change current directory : "{self.cwd.name}" -> "{newcwd.name}"')
                self.cwd = newcwd
            return
        if tokens[0] == "dir":  # dir info
            if self.verbose:
                print(f'found directory : "{tokens[1]}"')
            self.cwd.add_dir(Directory(tokens[1], parent=self.cwd))
        else:  # file info
            if self.verbose:
                print(f'found file : "{tokens[1]}"')
            self.cwd.add_file(File(tokens[1], int(tokens[0])))

    def parse(self):
        for i, line in enumerate(self.lines):
            if self.verbose:
                print(f"[{i:03d}] : {line}")
            self.parse_line(line)

parser = Parser(verbose=True)
parser.parse()

# Puzzle 1

def get_allsizes(d: Directory, sizes: list[int]):
    sizes.append(d.size())
    for d in d.directories.values():
        get_allsizes(d, sizes)
    return sizes

print(sum((x for x in get_allsizes(parser.root, []) if x <= 100000)))

# Puzzle 2

unused = 70000000 - parser.root.size()
reclaim = 30000000 - unused
print(min([x for x in get_allsizes(parser.root, []) if x >= reclaim]))

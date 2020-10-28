#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:20:30 2020
# Darkest dungeon
@author: mickael
"""


from pprint import pprint as pp
import random

def force_print(lab):
    for elt in lab:
        print("".join(elt))


class labyrinth():
    def __init__(self, x, y):
        # if x or y are even then += 1
        if not x & 1:
            x += 1
        if not y & 1:
            y += 1

        self.x = x
        self.y = y

        self.block = "▓"  # "█"
        self.not_block = " "
        self.direction = [[2, 0],
                          [-2, 0],
                          [0, 2],
                          [0, -2]]

    def is_outer_edge(self, pos):
        cond = [pos[0] == 0,
                pos[0] == self.x,
                pos[1] == 0,
                pos[1] == self.y]
        return any(cond)

    def is_in_lab(self, pos):
        return not self.is_outer_edge(pos)

    def gen_raw_lab(self):
        # █
        raw_lab = []
        for row in range(self.x):
            raw_lab.append([self.block]*self.y)
        self.lab = raw_lab

    def trace_path(self):
        start = [random.randrange(1,self.x,2),
                 random.randrange(1,self.y,2)]
        self.mv(start)

    def get_pos_path(self, pos):
        pos_path = []
        random.shuffle(self.direction)
        for d in self.direction:
            spot = [pos[0] + d[0],
                    pos[1] + d[1]]
            if spot[0] < 0 or spot[1] < 0 or spot[0] > self.x or spot[1] > self.y:
                continue
            if self.is_in_lab(spot) and self.lab[spot[0]][spot[1]] == self.block:
                # not in outer edge and not a path already seen
                pos_path.append((spot, d))
        return pos_path

    def mv(self, pos):
        for path in self.get_pos_path(pos):
            spot = path[0]
            if self.lab[spot[0]][spot[1]] != self.block:
                continue
            d = path[1]
            # print(spot, d)
            diff = [int(spot[0] - d[0]/2),
                    int(spot[1] - d[1]/2)]
            # print(diff)
            self.lab[diff[0]][diff[1]] = self.not_block
            self.lab[spot[0]][spot[1]] = self.not_block
            self.mv(spot)

    def set_start_end(self):
        start = (random.randint(1, self.x-1),
                 0)
        while self.lab[start[0]][start[1]+1] == self.block:
            start = (random.randint(1, self.x-1),
                     0)

        end = (random.randint(1, self.x-1),
               self.y-1)
        while self.lab[end[0]][end[1]-1] == self.block:
            end = (random.randint(1, self.x-1),
                   self.y-1)

        self.lab[start[0]][start[1]] = self.not_block
        self.lab[end[0]][end[1]] = self.not_block

    def main(self):
        self.gen_raw_lab()
        self.trace_path()
        self.set_start_end()
        force_print(lab.lab)


if __name__ == "__main__":
    lab = labyrinth(13, 30)
    lab.main()

# -*- coding: utf-8 -*-

import random
import networkx as nx

"""
# Théorie:
# 1 Choisir longueur max
# 2 Tirer x chemin supplémentaire
# 3 Profit $$$
"""


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


class graph_node:
    def __init__(self, node_id, origin, destination, floor):
        self.node_id = node_id
        # Z floor = distance from the start node
        self.floor = floor
        self.origin = origin
        self.destination = destination


class graph_world:
    def __init__(self):
        self.world = {}
        self.world_len = 7
        self.world["start"] = graph_node("start", [], [], 0)
        self.world["end"] = graph_node("end", [], [], self.world_len)
        # custom generator to get id
        self.new_id = infinite_sequence()

        # intialize the first path
        self.new_path(node_a_id='start', node_b_id='end')

    def give_id(self):
        return next(self.new_id)

    def add_node(self, node_id, previous, destination, floor):
        self.world[node_id] = graph_node(node_id, previous, destination, floor)

    def get_node(self, node_id):
        return self.world[node_id]

    def get_list_id(self):
        return self.world.keys()

    def choose_random_node_id(self):
        return random.choice(list(self.get_list_id()))

    def choose_random_node_id_away_from(self, floor, distance=1):
        """
        Randomly choose a node id which 'distance' nodes away.
        """
        list_node_id = []
        for node_id in self.world.keys():
            if abs(self.world[node_id].floor - floor) > distance:
                list_node_id.append(node_id)
        return random.choice(list_node_id)

    def add_destination(self, node, node_destination):
        self.world[node].destination.append(node_destination)

    def add_origin(self, node, node_origin):
        # unused so far
        self.world[node].origin.append(node_origin)

    def new_path(self, len_node=0, node_a_id="", node_b_id=""):
        """
        Create a new path from a node to another.
        """
        # len node doit etre au max la distance la plus courte entre ces 2 points
        #len_node = 2
        if not node_a_id and not node_b_id:
            node_a_id = self.choose_random_node_id()
            node_b_id = self.choose_random_node_id_away_from(self.world[node_a_id].floor)
        elif not node_a_id:
            node_a_id = self.choose_random_node_id_away_from(self.world[node_b_id].floor)
        elif not node_b_id:
            node_b_id = self.choose_random_node_id_away_from(self.world[node_a_id].floor)

        node_a = self.get_node(node_a_id)
        node_b = self.get_node(node_b_id)

        # if b is not after a # could custom the choose function but flemme
        if node_b.floor - node_a.floor < 0:
            node_a, node_b = node_b, node_a
            node_a_id, node_b_id = node_b_id, node_a_id

        previous_id = node_a_id
        current_id = self.give_id()
        next_id = self.give_id()

        self.add_destination(node_a_id, current_id)
        for i in range(node_a.floor + 1, node_b.floor - 1):
            self.add_node(current_id, [previous_id], [next_id], i)
            previous_id = current_id
            current_id = next_id
            next_id = self.give_id()

        # add last node to the path with the destination be node_b
        try:
            self.add_node(current_id, [previous_id], [node_b_id], i + 1)
        except UnboundLocalError:
            # if there was only one node to add then i was not set in the
            # for loop
            i = node_a.floor
            self.add_node(current_id, [previous_id], [node_b_id], i + 1)

        """
        # mieux mais marche pas

        # if more than two node
        print("a: ",node_a_id, node_b_id, node_b.floor - node_a.floor)
        if node_b.floor - node_a.floor > 2:
            previous_id = node_a_id
            current_id = self.give_id()
            next_id = self.give_id()
            self.add_node(current_id, [node_a_id], [next_id], node_a.floor + 1)

            self.add_destination(node_a_id, current_id)
            for i in range(node_a.floor + 2, node_b.floor - 1):
                previous_id = current_id
                current_id = next_id
                next_id = self.give_id()
                self.add_node(current_id, [previous_id], [next_id], i)

            previous_id = current_id
            current_id = next_id
            self.add_node(current_id, [previous_id], [node_b_id], node_b.floor - 1)

        # if two node
        elif node_b.floor - node_a.floor == 2:
            current_id = self.give_id()
            next_id = self.give_id()
            print(current_id, next_id)
            self.add_node(current_id, [node_a_id] , [next_id]  , node_a.floor + 1)
            self.add_node(next_id   , [current_id], [node_b_id], node_b.floor - 1)

        # else 1 node
        else:
            current_id = self.give_id()
            self.add_node(current_id, [node_a_id], [node_b_id], node_a.floor + 1)
        """

    def get_graph(self):
        dict_node = {}
        for elt in self.world.keys():
            dict_node[elt] = self.world[elt].destination
        return dict_node

    def get_graph_pos(self):
        pos = {}
        wbf = self.get_world_by_floor()
        for i in range(0, self.world_len + 1):
            j = 0
            for node in wbf[i]:
                pos[node] = (i, j)
                j += 1
        return pos

    def offset_calc(self, nb_node):
        return (nb_node - 1)*0.5

    def get_graph_pos_centered(self):
        pos = {}
        wbf = self.get_world_by_floor()

        max_node = max([len(elt) for elt in wbf.values()])
        offset = self.offset_calc(max_node)

        for i in range(0, self.world_len + 1):
            j = 0
            for node in wbf[i]:
                offset = self.offset_calc(len(wbf[i]))
                pos[node] = (i, j - offset)
                j += 1
        return pos

    def get_world_by_floor(self):
        wbf = {}
        for i in range(0, self.world_len + 1):
            wbf[i] = []
            for v in self.world.values():
                if v.floor == i:
                    wbf[i].append(v.node_id)
        return wbf

    def plot_graph(self):
        graph = self.get_graph()
        # pos = self.get_graph_pos()
        pos = self.get_graph_pos_centered()
        g = nx.DiGraph(graph)
        nx.draw_networkx(g, pos)

    def demo(self, nb_path=5):
        for _ in range(nb_path):
            self.new_path()
        print("World Graph generated with " + str(nb_path) + " paths.")
        self.plot_graph()


if __name__ == "__main__":
    a = graph_world()
    a.demo()

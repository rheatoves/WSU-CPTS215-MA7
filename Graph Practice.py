############################################
# Title: MA7 Graph Practice
# Author: Rhea Toves
# Version: 1.0
# Date: April 13, 2022
#
# Description: This program implements a
# weighted graph using an adjacency matrix
# representation.
############################################

import numpy

class Graph():
    def __init__(self):
        # This method initializes the vert_list and adjacency_matrix.
        self.vert_list = []
        self.adjacency_matrix = numpy.zeros([10,10])

    def add_vertex(self, key):
        # This method adds a vertex to the vert_list if it does not exist already.
        if self.vert_list.count(key) == 0:
            self.vert_list.append(key)

    def add_edge(self, v1, v2):
        # This method adds an edge of weight 1 between vertices v1 and v2, as well as v2 and v1 in the adj_matrix.
        self.add_vertex(v1)
        self.add_vertex(v2)

        max_vertex = max(v1, v2)
        length_vertex = len(self.adjacency_matrix)
        if max_vertex >= length_vertex:
            self.adjacency_matrix = numpy.pad(self.adjacency_matrix, pad_width=1)
        self.adjacency_matrix[v1][v2] = 1
        self.adjacency_matrix[v2][v1] = 1

    def __str__(self):
        # This method returns a string representation of the graph.
        print("Edges:")
        for x in range(len(self.adjacency_matrix)):
            for y in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[x][y] == 1:
                    print('(', x, ',', y, ')', sep='')

def main():
    g = Graph()
    g.add_edge(6, 4)
    g.add_edge(4, 5)
    g.add_edge(5, 2)
    g.add_edge(5, 1)
    g.add_edge(4, 3)
    g.add_edge(3, 2)
    g.add_edge(2, 1)
    g.__str__()

main()
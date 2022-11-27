from typing import List, Dict, Tuple
from numpy import zeros, subtract, delete, linalg


def _pair_in_list(pair: Tuple[str, str], items: List[Tuple[str, str]]) -> bool:
    return pair in items or (pair[1], pair[0]) in items


class Graph:
    def __init__(self, nodes: List[str], edge_nodes: List[str]):
        self._graph: Dict[str, str] = {}
        for i, node in enumerate(nodes):
            self._graph[node] = edge_nodes[i]

        self._edges: List[Tuple[str, str]] = []
        for key, value in self._graph.items():
            other_nodes = value.split(',')
            for node in other_nodes:
                if not _pair_in_list(pair=(key, node),
                                     items=self._edges) and node != '':
                    self._edges.append((key, node))

    @property
    def edges(self):
        return self._edges

    @property
    def graph(self):
        return self._graph

    @property
    def degree_matrix(self):
        dimension = len(self._graph)
        np_arr = zeros([dimension, dimension], dtype=int)
        for i, node in enumerate(self._graph.keys()):
            np_arr[i][i] = len(self._graph[node].split(','))
        return np_arr

    @property
    def adjacency_matrix(self):
        dimension = len(self._graph)
        diff = ord('a')
        matrix = zeros([dimension, dimension], dtype=int)
        for i, node in enumerate(self._graph.keys()):
            neighbors = self._graph[node].split(',')
            for neighbor_node in neighbors:
                row_index = ord(neighbor_node) - diff
                matrix[row_index][i] = '1'
        return matrix

    def incidence_matrix(self, oriented: bool = False):
        dimensions = [len(self._graph), len(self.edges)]
        matrix = zeros(dimensions, dtype=int)
        for i, edge in enumerate(self.edges):
            if node := edge[0]:
                matrix[ord(node) - ord('a')][i] = 1
            if node := edge[1]:
                matrix[ord(node) - ord('a')][i] = -1 if oriented else 1

        return matrix

    @property
    def laplacian_matrix(self):
        return subtract(self.degree_matrix, self.adjacency_matrix)

    @property
    def spanning_trees_count(self):
        det_matrix = delete(self.laplacian_matrix, 0, 0)
        det_matrix = delete(det_matrix, 0, 1)
        return int(linalg.det(det_matrix))

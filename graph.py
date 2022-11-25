from typing import List, Dict, Tuple
from numpy import zeros, subtract, delete, linalg


def _pair_in_list(pair: Tuple[str, str], lst: List[Tuple[str, str]]) -> bool:
    return pair in lst or (pair[1], pair[0]) in lst


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
                                     lst=self._edges):
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
        np_arr = zeros([dimension, dimension], dtype=int)
        for i, node in enumerate(self._graph.keys()):
            neighbors = self._graph[node].split(',')
            for neighbor_node in neighbors:
                idx = ord(neighbor_node) - diff
                np_arr[idx][i] = '1'
        return np_arr

    @property
    def incidence_matrix(self):
        dimensions = [len(self._graph), len(self.edges)]
        np_arr = zeros(dimensions, dtype=int)
        for i, edge in enumerate(self.edges):
            np_arr[ord(edge[0]) - ord('a')][i] = 1
            np_arr[ord(edge[1]) - ord('a')][i] = 1

        return np_arr

    @property
    def laplacian_matrix(self):
        return subtract(self.degree_matrix, self.adjacency_matrix)

    @property
    def spanning_trees_count(self):
        det_matrix = delete(self.laplacian_matrix, 0, 0)
        det_matrix = delete(det_matrix, 0, 1)
        return linalg.det(det_matrix)

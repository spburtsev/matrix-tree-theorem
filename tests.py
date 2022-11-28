from unittest import TestCase

from graph import Graph
from test_data import (MATRIX_THEOREM_UNORIENTED_GRAPH_ADJACENCY_MATRIX,
                       MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED,
                       MATRIX_THEOREM_UNORIENTED_GRAPH_SPANNING_TREES,
                       UNORIENTED_GRAPH, UNORIENTED_GRAPH_ADJACENCY_MATRIX,
                       UNORIENTED_GRAPH_INCIDENCE_MATRIX,
                       UNORIENTED_GRAPH_PARSED,
                       UNORIENTED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX,
                       UNORIENTED_GRAPH_WITH_LOOPS_PARSED)
from util import parse_edge_nodes, parse_nodes


class ParseNodesTest(TestCase):
    def test_parse_nodes_1(self):
        nodes = parse_nodes('a,b,c')
        self.assertEqual(nodes, ['a', 'b', 'c'])

    def test_parse_nodes_2(self):
        nodes = parse_nodes('a,  b ,c    ,d , e ,f   ,g  ,h  ,i , j')
        self.assertEqual(
            nodes, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])

    def test_parse_3(self):
        nodes = parse_nodes(UNORIENTED_GRAPH['nodes'])
        self.assertEqual(nodes, UNORIENTED_GRAPH_PARSED['nodes'])

    def test_parse_4(self):
        egdes = parse_edge_nodes(UNORIENTED_GRAPH['edges'])
        self.assertEqual(egdes, UNORIENTED_GRAPH_PARSED['edges'])

    def test_parse_5(self):
        nodes = parse_nodes(UNORIENTED_GRAPH['nodes'])
        egdes = parse_edge_nodes(UNORIENTED_GRAPH['edges'])

        graph_1 = Graph(nodes, egdes)
        graph_2 = Graph(UNORIENTED_GRAPH_PARSED['nodes'],
                        UNORIENTED_GRAPH_PARSED['edges'])

        self.assertEqual(graph_1.graph, graph_2.graph)
        self.assertEqual(graph_1.edges, graph_2.edges)


class TestingGraph(TestCase):
    def test_graph_1(self):
        graph = Graph(['a', 'b', 'c'], ['b', 'c', 'a'])
        self.assertEqual(len(graph.edges), 3)

    def test_graph_2(self):
        graph = Graph(['a', 'b', 'c'], ['b,c', 'a,c', 'a,b'])
        self.assertEqual(len(graph.edges), 3)

    def test_graph_3(self):
        graph = Graph(['a', 'b', 'c'], ['a,b,c', 'c', 'b'])
        self.assertEqual(len(graph.edges), 4)

    def test_graph_4(self):
        graph = Graph(UNORIENTED_GRAPH_WITH_LOOPS_PARSED['nodes'],
                      UNORIENTED_GRAPH_WITH_LOOPS_PARSED['edges'])
        self.assertEqual(len(graph.edges), 8)


class TestingSpanningTreesCount(TestCase):
    def test_st_1(self):
        graph = Graph(['a', 'b', 'c'], ['b', 'c', 'a'])
        self.assertEqual(graph.spanning_trees_count, 1)

    def test_st_2(self):
        graph = Graph(UNORIENTED_GRAPH_PARSED['nodes'],
                      UNORIENTED_GRAPH_PARSED['edges'])
        self.assertEqual(graph.spanning_trees_count, 418)

    def test_st_3(self):
        graph = Graph(
            MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED['nodes'],
            MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED['edges']
        )
        self.assertEqual(graph.spanning_trees_count,
                         MATRIX_THEOREM_UNORIENTED_GRAPH_SPANNING_TREES)


class TestingAdjacencyMatrix(TestCase):
    def test_am_1(self):
        graph = Graph(
            UNORIENTED_GRAPH_WITH_LOOPS_PARSED['nodes'],
            UNORIENTED_GRAPH_WITH_LOOPS_PARSED['edges'])
        matrix = graph.adjacency_matrix
        for i, el in enumerate(matrix):
            self.assertEqual(
                list(el), UNORIENTED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX[i])

    def test_am_2(self):
        graph = Graph(UNORIENTED_GRAPH_PARSED['nodes'],
                      UNORIENTED_GRAPH_PARSED['edges'])
        matrix = graph.adjacency_matrix
        for i, el in enumerate(matrix):
            self.assertEqual(list(el), UNORIENTED_GRAPH_ADJACENCY_MATRIX[i])

    def test_am_3(self):
        graph = Graph(
            nodes=MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED['nodes'],
            edge_nodes=MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED['edges']
        )
        matrix = graph.adjacency_matrix
        for i, el in enumerate(matrix):
            self.assertEqual(
                list(el),
                MATRIX_THEOREM_UNORIENTED_GRAPH_ADJACENCY_MATRIX[i]
            )


class TestingIncidenceMatrix(TestCase):
    def test_im_1(self):
        graph = Graph(
            ['a', 'b', 'c', 'd', 'e', 'f'],
            ['b,e', 'a,c,e', 'b,d', 'c,e,f', 'a,b,d', 'd'])
        matrix = graph.incidence_matrix()

        expected = [
            [1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
        for i, el in enumerate(matrix):
            self.assertEqual(list(el), expected[i])

    def test_im_2(self):
        graph = Graph(
            UNORIENTED_GRAPH_PARSED['nodes'],
            UNORIENTED_GRAPH_PARSED['edges'])
        matrix = graph.incidence_matrix()

        for i, el in enumerate(matrix):
            self.assertEqual(list(el), UNORIENTED_GRAPH_INCIDENCE_MATRIX[i])

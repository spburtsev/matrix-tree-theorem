from unittest import TestCase

from graph import Graph
from test_data import (UNORDERED_GRAPH, UNORDERED_GRAPH_ADJACENCY_MATRIX,
                       UNORDERED_GRAPH_INCIDENCE_MATRIX,
                       UNORDERED_GRAPH_PARSED,
                       UNORDERED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX,
                       UNORDERED_GRAPH_WITH_LOOPS_PARSED)
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
        nodes = parse_nodes(UNORDERED_GRAPH['nodes'])
        self.assertEqual(nodes, UNORDERED_GRAPH_PARSED['nodes'])

    def test_parse_4(self):
        egdes = parse_edge_nodes(UNORDERED_GRAPH['edges'])
        self.assertEqual(egdes, UNORDERED_GRAPH_PARSED['edges'])

    def test_parse_5(self):
        nodes = parse_nodes(UNORDERED_GRAPH['nodes'])
        egdes = parse_edge_nodes(UNORDERED_GRAPH['edges'])

        g1 = Graph(nodes, egdes)
        g2 = Graph(UNORDERED_GRAPH_PARSED['nodes'],
                   UNORDERED_GRAPH_PARSED['edges'])

        self.assertEqual(g1.graph, g2.graph)
        self.assertEqual(g1.edges, g2.edges)


class TestingGraph(TestCase):
    def test_graph_1(self):
        g = Graph(['a', 'b', 'c'], ['b', 'c', 'a'])
        self.assertEqual(len(g.edges), 3)

    def test_graph_2(self):
        g = Graph(['a', 'b', 'c'], ['b,c', 'a,c', 'a,b'])
        self.assertEqual(len(g.edges), 3)

    def test_graph_3(self):
        g = Graph(['a', 'b', 'c'], ['a,b,c', 'c', 'b'])
        self.assertEqual(len(g.edges), 4)

    def test_graph_4(self):
        g = Graph(UNORDERED_GRAPH_WITH_LOOPS_PARSED['nodes'],
                  UNORDERED_GRAPH_WITH_LOOPS_PARSED['edges'])
        self.assertEqual(len(g.edges), 8)


class TestingSpanningTreesCount(TestCase):
    def test_st_1(self):
        g = Graph(['a', 'b', 'c'], ['b', 'c', 'a'])
        self.assertEqual(g.spanning_trees_count, 1)

    def test_st_2(self):
        g = Graph(UNORDERED_GRAPH_PARSED['nodes'],
                  UNORDERED_GRAPH_PARSED['edges'])
        self.assertEqual(g.spanning_trees_count, 418)


class TestingAdjacencyMatrix(TestCase):
    def test_am_1(self):
        g = Graph(
            UNORDERED_GRAPH_WITH_LOOPS_PARSED['nodes'],
            UNORDERED_GRAPH_WITH_LOOPS_PARSED['edges'])
        am = g.adjacency_matrix
        for i, el in enumerate(am):
            self.assertEqual(
                list(el), UNORDERED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX[i])

    def test_am_2(self):
        g = Graph(UNORDERED_GRAPH_PARSED['nodes'],
                  UNORDERED_GRAPH_PARSED['edges'])
        am = g.adjacency_matrix
        for i, el in enumerate(am):
            self.assertEqual(list(el), UNORDERED_GRAPH_ADJACENCY_MATRIX[i])


class TestingIncidenceMatrix(TestCase):
    def test_im_1(self):
        g = Graph(
            ['a', 'b', 'c', 'd', 'e', 'f'],
            ['b,e', 'a,c,e', 'b,d', 'c,e,f', 'a,b,d', 'd'])
        im = g.incidence_matrix()

        expected = [
            [1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 1],
            [0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
        ]
        for i, el in enumerate(im):
            self.assertEqual(list(el), expected[i])

    def test_im_2(self):
        g = Graph(
            UNORDERED_GRAPH_PARSED['nodes'],
            UNORDERED_GRAPH_PARSED['edges'])
        im = g.incidence_matrix()

        for i, el in enumerate(im):
            self.assertEqual(list(el), UNORDERED_GRAPH_INCIDENCE_MATRIX[i])

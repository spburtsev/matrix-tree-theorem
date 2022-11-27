from graph import Graph
from test_data import (ORDERED_GRAPH_WITH_CYCLES, ORDERED_GRAPH_WITHOUT_CYCLES,
                       UNORDERED_GRAPH)
from util import PRINT_DELIMITER, parse_edge_nodes, parse_nodes

if __name__ == '__main__':
    node_parts = parse_nodes(UNORDERED_GRAPH['nodes'])
    edge_parts = parse_edge_nodes(UNORDERED_GRAPH['edges'])

    graph = Graph(node_parts, edge_parts)

    node_parts = parse_nodes(ORDERED_GRAPH_WITHOUT_CYCLES['nodes'])
    edge_parts = parse_edge_nodes(ORDERED_GRAPH_WITHOUT_CYCLES['edges'])
    graph_2 = Graph(node_parts, edge_parts)

    node_parts = parse_nodes(ORDERED_GRAPH_WITH_CYCLES['nodes'])
    edge_parts = parse_edge_nodes(ORDERED_GRAPH_WITH_CYCLES['edges'])
    graph_3 = Graph(node_parts, edge_parts)

    laplacian_matrix = graph.laplacian_matrix
    print('Laplacian Matrix:\n' + str(laplacian_matrix) + '\n' + PRINT_DELIMITER)
    print('Number of spanning trees: %d' % graph.spanning_trees_count)
    print(graph.incidence_matrix())
    print(PRINT_DELIMITER)
    print(graph_2.incidence_matrix(oriented=True))
    print(PRINT_DELIMITER)
    print(graph_3.incidence_matrix(oriented=True))

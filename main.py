from graph import Graph
from test_data import ORDERED_GRAPH_WITHOUT_CYCLES, UNORDERED_GRAPH
from util import PRINT_DELIMITER, parse_edge_nodes, parse_nodes

if __name__ == '__main__':
    node_parts = parse_nodes(UNORDERED_GRAPH['nodes'])
    edge_parts = parse_edge_nodes(UNORDERED_GRAPH['edges'])
    gr = Graph(node_parts, edge_parts)

    node_parts = parse_nodes(ORDERED_GRAPH_WITHOUT_CYCLES['nodes'])
    edge_parts = parse_edge_nodes(ORDERED_GRAPH_WITHOUT_CYCLES['edges'])
    gr2 = Graph(node_parts, edge_parts)

    laplacian_matrix = gr.laplacian_matrix
    print('Laplacian Matrix:\n' + str(laplacian_matrix) + '\n' + PRINT_DELIMITER)
    print('Number of spanning trees: %d' % gr.spanning_trees_count)
    print(gr.incidence_matrix())
    print(gr2.incidence_matrix(oriented=True))

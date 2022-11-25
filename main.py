import re
from typing import List

from graph import Graph
from util import PRINT_DELIMITER, remove_spaces


def retrieve_nodes() -> List[str]:
    # uncomment for user input
    # nodeString = input("Enter list of nodes (ex: \"a, b, c\": ")
    nodeString = "a,b,c,d,e,f,g,h,i,j"
    nodeString = remove_spaces(nodeString)
    return re.split(',', nodeString)


def retrieve_edge_nodes() -> List[List[str]]:
    # uncomment for user input
    # edgeString = input("Enter list of edges nodes corresponding to the order of the nodes (ex: \"[b, c], [a, c], [a, b]\"): ")
    edgeString = "[b,g],[a,c,f],[b,d,e],[c,e],[c,d,f],[b,e,g,i,j],[a,f,h],[g,i],[f,h,j],[f,i]"
    edgeString = remove_spaces(edgeString)
    edgeString = re.split('[\[\]]', edgeString)
    return [x for x in edgeString if x != '' and x != ',']


if __name__ == '__main__':
    nodeParts = retrieve_nodes()
    edgeParts = retrieve_edge_nodes()
    gr = Graph(nodeParts, edgeParts)
    laplacian_matrix = gr.laplacian_matrix
    print("Laplacian Matrix:\n" + str(laplacian_matrix) + '\n' + PRINT_DELIMITER)
    print("Number of spanning trees: %d" % gr.spanning_trees_count)
    print(gr.incidence_matrix)

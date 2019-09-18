import re
import numpy
import graph

def remove_spaces(line):
    return line.replace(' ', '')

def retrieve_nodes():
    # uncomment for user input
    # nodeString = input("Enter list of nodes (ex: \"a, b, c\": ")
    nodeString = "a, b, c, d, e, f, g, h, i"
    nodeString = remove_spaces(nodeString)
    return re.split(',', nodeString)

def retrieve_edge_nodes():
    # uncomment for user input
    # edgeString = input("Enter list of edges nodes corresponding to the order of the nodes (ex: \"[b, c], [a, c], [a, b]\"): ")
    edgeString = "[b, c, d, e], [a, c, d, e], [a, b, d, f, g], [a, b, c, e, f, g, h, i], " \
                 "[a, b, d, h, i], [c, d], [c, d], [d, e], [d, e]"
    edgeString = remove_spaces(edgeString)
    edgeString = re.split('[\[\]]', edgeString)
    return [[x] for x in edgeString if x != '' and x != ',']

def construct_graph(nodes, edges):
    return graph.Graph(nodes, edges)

def create_degree_matrix(g):
    dimension = len(g)
    count = 0
    np_arr = numpy.zeros([dimension, dimension], dtype=int)
    print(np_arr)
    for node in g.keys():
        np_arr[count][count] = len(g[node][0].split(','))
        count += 1
    return np_arr

def create_adjacency_matrix(g, ):
    dimension = len(g)
    count = 0
    diff = ord('a')
    np_arr = numpy.zeros([dimension, dimension], dtype=int)
    for node in g.keys():
        neighbors = g[node][0].split(',')
        for neighbor_node in neighbors:
            idx = ord(neighbor_node) - diff
            np_arr[idx][count] = '1'
        count += 1
    return np_arr

if __name__ == '__main__':
    nodeParts = retrieve_nodes()
    edgeParts = retrieve_edge_nodes()
    gr = construct_graph(nodeParts, edgeParts)
    degree_matrix = create_degree_matrix(gr.graph)
    adjacency_matrix = create_adjacency_matrix(gr.graph)
    # TODO: implement laplacian matrix using numpy.subtract(arr1, arr2)
    # TODO: implement determinant using numpy.linalg.det(arr)

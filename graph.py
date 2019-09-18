class Graph:
    def __init__(self, nodes, edgeNodes):
        self.nodes = nodes
        self.edgeNodes = edgeNodes
        self.graph = {}
        for i in range(len(nodes)):
            self.graph[nodes[i]] = edgeNodes[i]

    def generate_edges(self):
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                edges.append((node, neighbour))
        return edges

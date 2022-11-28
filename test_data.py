from typing import List, TypedDict


class UnparsedTestData(TypedDict):
    nodes: str
    edges: str


class ParsedTestData(TypedDict):
    nodes: List[str]
    edges: List[str]


UNORIENTED_GRAPH = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b,g],[a,c,f],[b,d,e],[c,e],[c,d,f],[b,e,g,i,j],[a,f,h],[g,i],[f,h,j],[f,i]'
)

UNORIENTED_GRAPH_PARSED = ParsedTestData(
    nodes=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    edges=['b,g', 'a,c,f', 'b,d,e', 'c,e', 'c,d,f',
           'b,e,g,i,j', 'a,f,h', 'g,i', 'f,h,j', 'f,i']
)
UNORIENTED_GRAPH_ADJACENCY_MATRIX = [
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 1, 0]
]
UNORIENTED_GRAPH_INCIDENCE_MATRIX = [
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
]


ORIENTED_GRAPH_WITHOUT_CYCLES = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b,g],[c,f],[d,e],[e],[f],[i,j],[f,h],[i],[j],[]'
)

ORIENTED_GRAPH_WITH_CYCLES = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b],[f],[b,d,e],[e],[f],[i,j],[a,f],[g],[h],[i]'
)

UNORIENTED_GRAPH_WITH_LOOPS_PARSED = ParsedTestData(
    nodes=['a', 'b', 'c', 'd', 'e', 'f'],
    edges=['a,b,e', 'a,c,e', 'b,d', 'c,e,f', 'a,b,d', 'd']
)
UNORIENTED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX = [
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

MATRIX_THEOREM_UNORIENTED_GRAPH_PARSED = ParsedTestData(
    nodes=['a', 'b', 'c', 'd'],
    edges=['b,c', 'a,c', 'a,b,d', 'c']
)
MATRIX_THEOREM_UNORIENTED_GRAPH_ADJACENCY_MATRIX = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
]
MATRIX_THEOREM_UNORIENTED_GRAPH_SPANNING_TREES = 3

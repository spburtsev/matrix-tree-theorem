from typing import List, TypedDict


class UnparsedTestData(TypedDict):
    nodes: str
    edges: str


class ParsedTestData(TypedDict):
    nodes: List[str]
    edges: List[str]


UNORDERED_GRAPH = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b,g],[a,c,f],[b,d,e],[c,e],[c,d,f],[b,e,g,i,j],[a,f,h],[g,i],[f,h,j],[f,i]'
)

UNORDERED_GRAPH_PARSED = ParsedTestData(
    nodes=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
    edges=['b,g', 'a,c,f', 'b,d,e', 'c,e', 'c,d,f',
           'b,e,g,i,j', 'a,f,h', 'g,i', 'f,h,j', 'f,i']
)
UNORDERED_GRAPH_ADJACENCY_MATRIX = [
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
UNORDERED_GRAPH_INCIDENCE_MATRIX = [
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


ORDERED_GRAPH_WITHOUT_CYCLES = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b,g],[c,f],[d,e],[e],[f],[i,j],[f,h],[i],[j],[]'
)

ORDERED_GRAPH_WITH_CYCLES = UnparsedTestData(
    nodes='a,b,c,d,e,f,g,h,i,j',
    edges='[b],[f],[b,d,e],[e],[f],[i,j],[a,f],[g],[h],[i]'
)

UNORDERED_GRAPH_WITH_LOOPS_PARSED = ParsedTestData(
    nodes=['a', 'b', 'c', 'd', 'e', 'f'],
    edges=['a,b,e', 'a,c,e', 'b,d', 'c,e,f', 'a,b,d', 'd']
)
UNORDERED_GRAPH_WITH_LOOPS_ADJACENCY_MATRIX = [
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

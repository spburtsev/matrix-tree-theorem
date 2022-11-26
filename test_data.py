from typing import TypedDict


class TestData(TypedDict):
    nodes: str
    edges: str


UNORDERED_GRAPH: TestData = {
    'nodes': 'a,b,c,d,e,f,g,h,i,j',
    'edges': '[b,g],[a,c,f],[b,d,e],[c,e],[c,d,f],[b,e,g,i,j],[a,f,h],[g,i],[f,h,j],[f,i]'
}

ORDERED_GRAPH_WITHOUT_CYCLES: TestData = {
    'nodes': 'a,b,c,d,e,f,g,h,i,j',
    'edges': '[b,g],[c,f],[d,e],[e],[f],[i,j],[f,h],[i],[j],[]'
}

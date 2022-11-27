from typing import List
from re import split

PRINT_DELIMITER = '-' * 50


def remove_spaces(line: str) -> str:
    return line.replace(' ', '')


def parse_nodes(s: str) -> List[str]:
    s = remove_spaces(s)
    return split(',', s)


def parse_edge_nodes(s: str) -> List[str]:
    s = remove_spaces(s)
    items = split(r'[\[\]]', s)
    items = items[1:-1]
    return [x for x in items if x != ',']

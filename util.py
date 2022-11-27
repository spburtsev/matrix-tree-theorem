from typing import List
from re import split

PRINT_DELIMITER = '-' * 50


def remove_spaces(line: str) -> str:
    return line.replace(' ', '')


def parse_nodes(text: str) -> List[str]:
    text = remove_spaces(text)
    return split(',', text)


def parse_edge_nodes(text: str) -> List[str]:
    text = remove_spaces(text)
    items = split(r'[\[\]]', text)
    items = items[1:-1]
    return [x for x in items if x != ',']

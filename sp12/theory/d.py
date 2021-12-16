# 60041259

def solution(node, elem: str) -> int:
    i = 0
    while node:
        if node.value == elem:
            return i
        node = getattr(node, 'next_item', None)
        i += 1
    return -1

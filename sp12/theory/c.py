# 60040476

def solution(node, idx: int) -> None:
    head = node
    if idx == 0:
        return head.next_item
    while idx:
        prev_node = node
        node = node.next_item
        idx -= 1
    n_item = getattr(node, 'next_item', None)
    prev_node.next_item = n_item
    return head

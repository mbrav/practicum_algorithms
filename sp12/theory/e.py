# 60134174

def solution(node):
    node.prev = None
    while node.next:
        if node.prev != None:
            node.next, node.prev = node.prev, node.next
        else:
            node.prev, node.next = node.next, None
        node = node.prev
    node.next = node.prev
    return node

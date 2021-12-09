# 60464500

from operator import methodcaller


def in_put(obj):
    x = int(input())
    arr = []
    for i in range(x):
        args = input().split()
        f = methodcaller(args[0])
        if len(args) == 2:
            f = methodcaller(args[0], int(args[1]))
        f(obj)
    return x, arr


class Queue:
    """Queue class for nodes"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    class Node:
        """Node Class"""

        def __init__(self, value=None, next=None, prev=None):
            self.value = value
            self.next = next

    def put(self, value):
        node = self.Node(value=value)
        if self.tail:
            self.tail.next = node
            self.tail = node
        if self.head == None:
            self.head = node
            self.tail = node
        self.count += 1

    def get(self):
        if self.head and self.count > 0:
            print(self.head.value)
            self.head = self.head.next
            self.count -= 1
        else:
            print('error')

    def size(self):
        print(self.count)


if __name__ == '__main__':
    queue = Queue()
    in_put(queue)

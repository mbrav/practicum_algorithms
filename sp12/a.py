# 61421264

import operator
from collections import deque


def in_put():
    x = int(input())
    y = int(input())
    obj = SuperMegaDeck(size=y)
    for i in range(x):
        args = input().split()
        f = operator.methodcaller(args[0])
        if len(args) == 2:
            f = operator.methodcaller(args[0], int(args[1]))
        f(obj)
    return x, y


class SuperMegaDeck():
    def __init__(self, size):
        self.size = size
        self.qeue = deque(maxlen=size)

    def push_front(self, val):
        if len(self.qeue) < self.size:
            self.qeue.append(val)
            return val
        print('error')

    def push_back(self, val):
        if len(self.qeue) < self.size:
            self.qeue.appendleft(val)
            return val
        print('error')

    def pop_front(self):
        if self.count():
            popped = self.qeue.pop()
            print(popped)
            return popped
        print('error')

    def pop_back(self):
        if self.count():
            popped = self.qeue.popleft()
            print(popped)
            return popped
        print('error')

    def count(self):
        return len(self.qeue)


if __name__ == '__main__':
    in_put()

# nnnnnnn

import operator
from collections import deque

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.div,
}


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
        self.qeue = deque()

    def push_front(self, val):
        return self.qeue.append(val)

    def push_back(self, val):
        return self.qeue.appendleft(val)

    def pop_front(self):
        if self.count():
            popped = self.qeue.pop()
            print(popped)
            return popped
        return 'error'

    def pop_back(self):
        if self.count():
            popped = self.qeue.popleft()
            print(popped)
            return popped
        return 'error'

    def count(self):
        return len(self.qeue)


if __name__ == '__main__':
    # in_put()
    x = 5
    methodToCall = getattr(math, 'sin')
    result = methodToCall(x)

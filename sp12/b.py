# 61428598

import operator
from collections import deque
from typing import List, Union
Number = Union[int, float]

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
    # '/': operator.truediv,
}


def calc(operation: str, *args: Number) -> Number:
    op = operations[operation]

    if len(args) == 1:
        return op(args[0], args[0])
    if len(args) == 2:
        return op(args[0], args[1])

    # Екстра функционал для вычислений больше двух аргументов
    #  ¯\_(ツ)_/¯
    result = None
    for a in range(1, len(args)):
        if a == 1:
            result = op(args[a-1], args[a])
        else:
            result = op(result, args[a])
    return result


class StackMinimalochka():
    def __init__(self):
        self.qeue = deque()

    def push(self, val):
        return self.qeue.append(val)

    def pop(self):
        if self.count():
            popped = self.qeue.pop()
            return popped
        print('error')

    def count(self):
        return len(self.qeue)

    def __str__(self):
        return str(f'{len(self.qeue)} objects in Stack')


def in_put(string: str = None) -> List:
    if string:
        return string.split()
    return input().split()


if __name__ == '__main__':
    # inputs = in_put('2 5 - 4 /')
    inputs = in_put()
    stack = StackMinimalochka()
    for i in inputs:
        if i in operations:
            y = stack.pop()
            x = stack.pop()
            result = calc(i, x, y)
            stack.push(result)
        else:
            stack.push(int(i))
    result = int(stack.pop())

    print(result)

# 61691770

import operator
from typing import List, Union

Number = Union[int, float]

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
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


class QueueMinimalochka():
    def __init__(self):
        self.queue = []

    def append(self, val):
        return self.queue.append(val)

    def pop(self):
        if self.count():
            popped = self.queue.pop()
            return popped
        print('error')

    def count(self):
        return len(self.queue)

    def __str__(self):
        return str(f'{len(self.queue)} objects in Queue')


def in_put(string: str = None) -> List:
    if string:
        return string.split()
    return input().split()


def run(inputs: List[str]) -> Number:
    queue = QueueMinimalochka()
    for i in inputs:
        if i in operations:
            y = queue.pop()
            x = queue.pop()
            result = calc(i, x, y)
            queue.append(result)
        else:
            queue.append(int(i))
    return int(queue.pop())


if __name__ == '__main__':
    inputs = in_put()
    result = run(inputs)
    print(result)

# 60351395

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


class MaxEffective:
    def __init__(self):
        self.items = []

    def push(self, item):
        if self.items:
            if item >= self.items[-1]:
                self.items.append(item)
            else:
                self.items.append(self.items[-1])
        else:
            self.items.append(item)

    def pop(self):
        if self.items:
            self.items.pop()
        else:
            print('error')

    def get_max(self):
        if self.items:
            print(self.items[-1])
        else:
            print('None')


if __name__ == "__main__":
    stack = MaxEffective()
    in_put(stack)

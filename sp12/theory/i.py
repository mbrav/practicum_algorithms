# 60439789

from operator import methodcaller


def in_put(obj):
    x = int(input())
    y = int(input())
    arr = []
    obj.setup(y)
    for i in range(x):
        args = input().split()
        f = methodcaller(args[0])
        if len(args) == 2:
            f = methodcaller(args[0], int(args[1]))
        # print(args)
        f(obj)
    return x, y, arr


class MyQueueSized:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.siz = 0

    def setup(self, n):
        self.queue = [None] * n
        self.max_n = n

    def push(self, item):
        if self.siz != self.max_n:
            self.queue[self.tail] = item
            self.tail = (self.tail + 1) % self.max_n
            self.siz += 1
            return item
        print('error')

    def pop(self):
        if self.siz == 0:
            print('None')
            return None
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.siz -= 1
        print(item)
        return item

    def peek(self):
        print(self.queue[self.head])

    def size(self):
        print(self.siz)


if __name__ == '__main__':
    queue = MyQueueSized()
    in_put(queue)

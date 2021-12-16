# 61402899

from operator import methodcaller
from collections import deque


def in_put():
    x = int(input())
    y = int(input())
    obj = SuperMegaDeck(size=y)
    for i in range(x):
        args = input().split()
        f = methodcaller(args[0])
        if len(args) == 2:
            f = methodcaller(args[0], int(args[1]))
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
        return 'error'

    def push_back(self, val):
        if len(self.qeue) < self.size:
            self.qeue.appendleft(val)
            return val
        print('error')
        return 'error'

    def pop_front(self):
        if self.count():
            popped = self.qeue.pop()
            print(popped)
            return popped
        print('error')
        return 'error'

    def pop_back(self):
        if self.count():
            popped = self.qeue.popleft()
            print(popped)
            return popped
        print('error')
        return 'error'

    def count(self):
        # print(len(self.qeue))
        return len(self.qeue)


if __name__ == '__main__':
    in_put()

    # deck = SuperMegaDeck(size=8)
    # deck.push_front(842)
    # deck.pop_back()
    # deck.push_front(576)
    # deck.push_front(-853)
    # deck.pop_back()
    # deck.push_front(123)
    # deck.push_front(-236)
    # deck.pop_front()
    # deck.push_back(840)
    # deck.pop_front()
    # deck.push_back(740)
    # deck.push_back(347)
    # deck.pop_front()
    # deck.push_front(-767)
    # deck.push_front(-711)
    # deck.push_back(-7)
    # deck.pop_front()
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_front()
    # deck.push_back(-215)
    # deck.push_front(540)
    # deck.pop_front()
    # deck.push_front(-293)
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_front()
    # deck.pop_back()
    # deck.push_back(873)
    # deck.push_front(47)
    # deck.push_back(-238)
    # deck.push_front(-575)
    # deck.pop_front()
    # deck.push_front(-916)
    # deck.push_front(292)
    # deck.push_back(302)
    # deck.push_front(456)
    # deck.push_back(92)
    # deck.push_back(-422)
    # deck.push_back(890)
    # deck.push_back(-100)
    # deck.pop_back()
    # deck.push_front(-356)
    # deck.pop_front()
    # deck.push_front(430)
    # deck.push_front(469)
    # deck.push_back(-56)
    # deck.push_front(273)
    # deck.pop_back()
    # deck.pop_back()
    # deck.push_front(-397)
    # deck.push_back(131)
    # deck.pop_front()
    # deck.push_back(-4)
    # deck.push_front(-265)
    # deck.push_back(10)
    # deck.push_back(-531)
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.push_front(766)
    # deck.pop_front()
    # deck.push_front(-520)
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.pop_back()
    # deck.push_front(-386)
    # deck.push_back(-320)
    # deck.push_back(21)
    # deck.pop_front()
    # deck.push_back(495)
    # deck.pop_front()
    # deck.push_front(-95)
    # deck.pop_front()
    # deck.pop_back()
    # deck.push_back(908)
    # deck.push_front(115)

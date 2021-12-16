# nnnnnnnn
from functools import lru_cache


def in_put():
    res = list(map(int, input().split()))
    return res[0], res[1]


def fibo(n, n2):
    a = 1
    b = 1
    c = 0
    if n < 2:
        return a
    else:
        b = 2
        for i in range(2, n):
            c = a + b
            a = b
            b = c
    return b % pow(10, n2)


def fibo2(n, n2):
    @lru_cache(None)
    def fib(n):
        if n in (0, 1):
            return 1
        if n & 1:
            return fib((n+1)//2 - 1) * (2*fib((n+1)//2) - fib((n+1)//2 - 1))
        a, b = fib(n//2 - 1), fib(n//2)
        return a**2 + b**2
    if n < 2:
        return 1
    return fib(n) % pow(10, n2)


if __name__ == '__main__':
    x, y = in_put()
    print(fibo2(x, y))
    # print(fibo2(10, 1))

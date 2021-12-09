# 60468005

def in_put():
    x = int(input())
    return x


def fibo(num):
    a = 1
    b = 1
    c = 0
    if num < 2:
        print(a)
    else:
        b = 2
        for i in range(2, num):
            c = a + b
            a = b
            b = c
        print(b)


if __name__ == '__main__':
    fibo(in_put())

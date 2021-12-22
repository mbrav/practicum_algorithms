# 62392844

def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]

    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def t(sides: list):
    a, b, c = sides.pop(), sides.pop(), sides.pop()
    while b+c <= a:
        if not sides:
            return 0
        a, b, c = b, c, sides.pop()
    result = a+b+c
    return result


def t_recursive(sides: list, a: int, b: int, c: int):
    if not sides:
        return a+b+c
    a, b, c = b, c, sides.pop()
    t_recursive(sides, a, b, c)

    return t_recursive(sides, a, b, c)


def t_recursive2(sides: list, a: int = None, b: int = None, c: int = None):
    if not a or not b or not c:
        a, b, c = sides.pop(), sides.pop(), sides.pop()
    if not sides:
        return a+b+c
    a, b, c = b, c, sides.pop()
    t_recursive2(sides, a, b, c)

    return t_recursive2(sides, a, b, c)


def main(sides: list = None):
    if not sides:
        sides = in_put('93 89 96 18 65 55 17 4 30 2 78 54 36 72 87 94 36 30 74 45 76 27 39 48 3 93 46 27 58 61 29 42 46 6 47 94 43 56 91 16 78 20 15 68 89 13 9 34 83 93 62 50 42 63 72 13 98 59 3 10 94 63 56 98 33 7 76 90 54')
    sides = sorted(map(lambda x: int(x), sides))
    result = t(sides)
    # result = t_recursive(sides, sides.pop(), sides.pop(), sides.pop())
    # result = t_recursive2(sides)
    return result


if __name__ == '__main__':
    # a = in_put()
    # b = in_put()
    # print(main(b))
    print(main())

# 62355479


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]

    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def run(greed, cookie_sizes):
    cookie_sizes = map(lambda x: int(x), cookie_sizes)
    greed = map(lambda x: int(x), greed)

    cookie_sizes = sorted(cookie_sizes)
    greed = sorted(greed)

    happiness = 0
    i = 0
    for j in range(len(cookie_sizes)):
        if i == len(greed):
            break
        if cookie_sizes[j] >= greed[i]:
            happiness += 1
            i += 1
    return happiness


def main(greed=None, cookie_sizes=None):
    if not greed or not cookie_sizes:
        greed = in_put(
            '39 82 14 63 46 7 63 44 2 50 91 17 75 28 78 9 45 66 77 82 90 68 48 19 64 63 12 77 75 84 10 86 39 62 34 18 22 95 43 58 89 61 64 11 91 2 23 31 12 49')
        cookie_sizes = in_put(
            '22 72 2 39 82 69 61 95 90 53 80 96 13 63 49 55 21 41 8 99 16 4 24 96 69 91 55 13 58 97 72 69 6 84 73 5 43 52 41 7 22 70 21 74 64 26')

    result = run(greed, cookie_sizes)
    return result  # 43


if __name__ == '__main__':
    a = in_put()
    b = in_put()
    c = in_put()
    d = in_put()
    print(main(b, d))
    # print(main())

# nnnnnnn

def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]

    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def run(budget, prices):
    pass


def main(budget=None, prices=None):
    return result


if __name__ == '__main__':
    # a = in_put()
    # b = in_put()
    # print(main(a[1], b))
    print(main())

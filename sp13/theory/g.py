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


def main(clothes: list = None):
    if not clothes and not len(clothes) == 0:
        clothes = in_put('0 2 1 2 0 0 1')
    clothes = sorted(clothes)
    result = " ".join(clothes)
    return result


if __name__ == '__main__':
    a = in_put()
    b = in_put()
    print(main(b))
    # print(main())

# nnnnnn

def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return list(map(lambda x: int(x), st))
        return int(st[0])
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def main(inputs: list[int]):
    return inputs


if __name__ == '__main__':
    inputs = in_put()
    result = main(inputs)
    print(result)

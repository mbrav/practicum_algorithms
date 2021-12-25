# 62883340

def in_put(string: str = None):
    def str_or_inputs(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return list(map(lambda x: int(x), st))
        return int(st[0])
    if string:
        return str_or_inputs(string)
    return str_or_inputs(input())


def in_put_multi(ins: int):
    inputs = []
    for i in range(int(ins)):
        inputs.append(in_put())
    return inputs


def main(inputs):
    inputs = sorted(inputs, key=lambda arr: arr[0])
    result = [inputs[0]]
    for i in range(1, len(inputs)):
        if result[-1][1] >= inputs[i][0]:
            result[-1][1] = max(result[-1][1], inputs[i][1])
        else:
            result.append(inputs[i])
    return result


if __name__ == '__main__':
    a = in_put()
    inputs = in_put_multi(a)

    # a = in_put('6')
    # inputs = [
    #     [1, 3],
    #     [3, 5],
    #     [4, 6],
    #     [5, 6],
    #     [2, 4],
    #     [7, 10],
    # ]

    for i in main(inputs):
        print(*i)

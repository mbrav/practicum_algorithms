# 62360817


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
    count = 0
    for p in prices:
        if p <= budget:
            budget -= p
            count += 1
        else:
            break
    return count


def main(budget=None, prices=None):
    if not budget or not prices:
        budget = in_put(
            '3 1000')[1]
        prices = in_put(
            '350 999 200')

    prices = sorted(map(lambda x: int(x), prices))
    result = run(int(budget), prices)
    return result  # 2


if __name__ == '__main__':
    a = in_put()
    b = in_put()
    print(main(a[1], b))
    # print(main())

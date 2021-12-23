# 62475705

from collections import Counter
from typing import List


def conference(uni_ids: List[str], top_n: int):
    result = Counter(uni_ids)
    result = sorted(result, key=result.get, reverse=True)
    return result[:top_n]


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def main(uni_ids: list = None, top_n: int = None):
    if not uni_ids or not top_n:
        uni_ids = in_put(
            '1 1 1 2 2 3 7 5 5')
        top_n = in_put(
            '3')
    return ' '.join(conference(uni_ids, int(top_n)))


if __name__ == '__main__':
    # a = in_put()
    # b = in_put()
    # c = in_put()
    # print(main(b, c))
    print(main())

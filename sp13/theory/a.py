# 62280642

from typing import List, Union

Number = Union[int, float]


def in_put(string: str = None) -> int:
    if string:
        return int(string)
    return int(input())


def braket(n: int) -> str:
    def run(left, right, s):
        if right == n:
            yield from s
            return
        if left < n:
            yield from run(left + 1, right, s + "(")
        if right < left:
            yield from run(left, right + 1, s + ")")
    yield from run(0, 0, "")


def split_strings(brakets: str, num: Number) -> List:
    variations = []
    for i in range(0, len(brakets), num):
        variations.append(brakets[i: i+num])
    return variations


def main(number: int = None):
    if not number:
        number = in_put('8')
    brakets = "".join([result for result in braket(number)])
    return split_strings(brakets, number*2)


if __name__ == '__main__':
    number = in_put()
    for var in main(number):
        print(var)

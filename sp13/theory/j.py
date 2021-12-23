# 62525974

from typing import List


def bubble_sort(numbers: List[int]):
    n = len(numbers)
    count = 0
    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                sorted = False
        if sorted:
            break
        yield numbers
        count += 1
    if count == 0:
        yield numbers


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def main(numbers: list = None):
    if not numbers:
        numbers = in_put(
            '4 5')

    numbers = list(map(lambda x: int(x), numbers))
    results = bubble_sort(numbers)
    for res in results:
        to_str = list(map(lambda x: str(x), res))
        print(' '.join(to_str))


if __name__ == '__main__':
    # a = in_put()
    # b = in_put()
    # main(b)
    main()

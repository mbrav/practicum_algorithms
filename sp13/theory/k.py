# nnnnnnn

from typing import List


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        # if len(st) > 1:
        #     return st
        # return st[0]
        return st
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def merge(arr: list, left: int, mid: int, right: int) -> list:
    # Your code
    # “ヽ(´▽｀)ノ”
    right = len(arr)
    mid = right // 2
    arr1, arr2 = arr[left:mid], arr[mid:right]
    i = j = 0
    result = []
    while i < mid - left and j < right - mid:
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:] + arr2[j:]
    return result


def merge_sort(arr: list, left: int, right: int) -> None:
    # Your code
    # “ヽ(´▽｀)ノ”
    if left != 0 or right != len(arr):
        arr = arr[left: right]
    arr = sorted(arr)
    return arr


def main():
    a = in_put()
    b = in_put()
    c = in_put()
    d = in_put()

    numbers = list(map(lambda x: int(x), c))
    result = merge_sort(numbers, 0, len(numbers))
    result = list(map(lambda x: str(x), result))
    # print(' '.join(result))


if __name__ == '__main__':
    main()

# nnnnnn

from bisect import bisect_left


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return list(map(lambda x: int(x), st))
        return int(st[0])
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


# Linear Search
def linear(arr: list, target: int):
    for index, val in enumerate(arr):
        if val == target:
            return index
    return -1


# Binary Recursive Search
def binary_recursive(arr: list, target: int, left: int, right: int):
    if left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            return binary_recursive(arr, target, mid + 1, right)
        elif arr[mid] > target:
            return binary_recursive(arr, target, left, mid - 1)
    return -1


def broken_search(nums: list, target: int) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    if len(nums) < 3:
        return linear(nums, target)
    else:
        return binary_recursive(nums, target, 0, len(nums) - 1)


def main(nums: list = None, target: int = None):
    if not nums or not target:
        # nums = in_put(
        #     '19 21 100 101 1 4 5 7 12')
        # target = in_put('5')
        nums = in_put(
            '2472 2473 2486 2534 2628 2977 3016 3155 3215 3383 3522 3533 3572 3599 3754 3856 3888 3890 4082 4130 4155 4207 4555 4556 4594 4597 4854 4861 4948 5085 5107 5251 5257 5378 5408 5452 5484 5584 5626 5701 5760 5781 5851 5855 6025 6047 6133 6243 6296 6314 6409 6516 6521 6659 6735 6813 6917 7059 7120 7296 7310 7345 7360 7379 7425 7498 7693 7925 7993 8035 8165 8277 8310 8363 8544 8562 8774 8827 8860 8952 9163 9177 9255 9793 9894 199 213 227 429 465 498 728 939 1502 1744 1768 1821 2317 2428 2471')
        target = in_put('227')
    return broken_search(nums, target)


if __name__ == '__main__':
    print(main())
    pass

# 62919854

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


# Рекурсивный бинарный поиск
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


# Поиск индекса начала плохой части списка
def get_bad_index(arr: list) -> int:
    begin = 0
    for i, val in enumerate(arr[:-1]):
        if val > arr[i+1]:
            begin = i+1
            break
    return begin


# Рекурсивный бинарный поиск индекса начала плохой части списка
def get_bad_index_bin(arr: list, target: int, left: int, right: int):
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

    # if len(nums) < 500:
    #     if target in nums:
    #         return nums.index(target)
    #     return -1

    bad_i = get_bad_index(nums)
    if bad_i:
        badnums = nums[bad_i:]
        found = binary_recursive(badnums, target, 0, len(badnums) - 1)
        if found != -1:
            return found + bad_i
        nums = nums[:-bad_i]

    return binary_recursive(nums, target, 0, len(nums) - 1)


def main(nums: list = None, target: int = None):
    if not nums or not target:
        nums = in_put(
            '3271 3298 3331 3397 3407 3524 3584 3632 3734 3797 3942 4000 4180 4437 4464 4481 4525 4608 4645 4803 4804 4884 4931 4965 5017 5391 5453 5472 5671 5681 5959 6045 6058 6301 6529 6621 6961 7219 7291 7372 7425 7517 7600 7731 7827 7844 7987 8158 8169 8265 8353 8519 8551 8588 8635 9209 9301 9308 9336 9375 9422 9586 9620 9752 9776 9845 9906 9918 16 25 45 152 199 309 423 614 644 678 681 725 825 830 936 1110 1333 1413 1617 1895 1938 2107 2144 2184 2490 2517 2769 2897 2970 3023 3112 3156')
        target = in_put('25')
    return broken_search(nums, target)  # 69


if __name__ == '__main__':
    print(main())
    pass

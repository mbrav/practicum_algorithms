# 62919854
# Отравля a.py, b.py ещё решаю
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


# Бинарный поиск
def binary_search(arr: list, target: int):
    left = mid = 0
    right = len(arr) - 1
    while left <= right:
        mid = (right + left) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


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


# Бинарный поиск индекса начала плохой части списка
def get_bad_index(arr: list, target: int):
    if len(arr) < 3:
        if target in arr:
            return arr.index(target)
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle + 1
        elif arr[middle] > target:
            right = middle - 1


# Рекурсивный бинарный поиск индекса начала плохой части списка
def get_bad_index_bin(arr: list):
    def run(array: list, left: int, right: int):
        if left <= right:
            mid = (left + right) // 2
            if array[mid] > array[mid+1]:
                return mid
            if array[left] > array[mid]:
                return run(array, left+1, mid)
            elif array[mid] > array[left]:
                return run(array, mid, right-1)
        return -1
    return run(arr, 0, len(arr)-1)


def broken_search(nums: list, target: int) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    # bad_i = get_bad_index_bin(nums)
    # if bad_i != -1:
    #     badnums = nums[bad_i:]
    #     found = binary_recursive(badnums, target, 0, len(badnums) - 1)
    #     if found != -1:
    #         return found + bad_i
    #     nums = nums[:-bad_i]

    return binary_search(nums, target)
    # return binary_recursive(nums, target, 0, len(nums) - 1)


def main(nums: list = None, target: int = None):
    if not nums or not target:
        nums = in_put(
            '5 1')
        target = in_put('1')
    return broken_search(nums, target)  # 69


if __name__ == '__main__':
    print(main())

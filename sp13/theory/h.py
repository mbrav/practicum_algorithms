# 62452515

from typing import List


def max_num_from_list(nums: List[str]):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            swap = int(nums[j] + nums[j + 1]) < int(nums[j + 1] + nums[j])
            if swap:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return st
        return st[0]
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def main(nums: list = None):
    if not nums:
        nums = in_put(
            '9 18 1 65 51 16 6 43 6 36 7 11 64 5 1 76 15 11 11 15 57 95 3 49 92 78 83 51 10 3')
    return ''.join(max_num_from_list(nums))


if __name__ == '__main__':
    # a = in_put()
    # b = in_put()
    # print(main(b))
    print(main())

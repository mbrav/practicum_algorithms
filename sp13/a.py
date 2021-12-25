# nnnnnn


def in_put(string: str = None):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return list(map(lambda x: int(x), st))
        return int(st[0])
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def broken_search(nums: list, target: int) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    # Linear Search
    # for index, val in enumerate(nums):
    #     if val == target:
    #         return index
    # return -1

    # Bisect
    # import bisect
    # index = bisect.bisect_left(nums, target)
    # if index < len(nums) and nums[index] == target:
    #     return index

    def recursive(left, right):
        if left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                return recursive(mid + 1, right)
            elif nums[mid] > target:
                return recursive(left, mid - 1)
        return -1
    return recursive(0, len(nums) - 1)


def main(nums: list = None, target: int = None):
    if not nums or not target:
        nums = in_put(
            '19 21 100 101 1 4 5 7 12')
        target = in_put('5')
    return broken_search(nums, target)


if __name__ == '__main__':
    # print(main())
    pass
    # a = in_put()
    # b = in_put()
    # c = in_put()
    # print(main(c, b))

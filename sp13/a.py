# 63389117

def broken_search(nums: list, target: int) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    target = int(target)

    if len(nums) < 3:
        if target in nums:
            return nums.index(target)
        return -1

    def binary_search(arr: list, target: int):
        """Бинарный поиск"""
        left = mid = 0
        right = len(arr) - 1
        while left <= right:
            mid = (right + left) // 2
            if int(arr[mid]) < target:
                left = mid + 1
            elif int(arr[mid]) > target:
                right = mid - 1
            else:
                return mid
        return -1

    def get_bad_index(array: list):
        """Бинарный поиск индекса начала плохой части списка
        В отличии от простого бинарного поиска, он не ищет искомую цифру
        А цифру, которая расположена не по возрастанию
        """
        left, right = 0, len(array) - 1
        while left != right-1:
            mid = (left + right) // 2
            # print(left, mid, right)
            if int(array[mid]) > int(array[mid+1]):
                return mid+1
            if int(array[left]) > int(array[mid]):
                right = mid
            else:
                left = mid
        return -1

    # Получаем индекс начала плохой части списка
    bad_i = get_bad_index(nums)
    if bad_i != -1:
        found = binary_search(nums[bad_i:], target)
        if found != -1:
            return found + bad_i
        # Сокращаем список с уже проверенными числами
        nums = nums[:bad_i]

    return binary_search(nums, target)

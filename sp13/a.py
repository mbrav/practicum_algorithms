# 63183231

# Отравляю a.py, b.py ещё решаю
# Извиняюсь, до этого отправил пустое решение
#
# Мне совсем не ясно почему я получаю TL ошибку
# Я реализовал два поиска: binary_search() и get_bad_index()
# Оба используют бинарный поиск
# Второй используют модифицированию версию бинарного поиска
# Тесты, которые я мог проверить, все работают
# По моим тестам они явно работают за O(log n):
# Если посмотреть profiler.py:
# То там массив с 200'000 цифрами спокойно обрабатывается за <0.001 секунды
# Но мне не ясно почему я получаю TL в 1 секунду, а проверить не могу так как:
# "File is too long to be displayed fully"
#
# С праздниками!

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


# Бинарный поиск индекса начала плохой части списка
def get_bad_index(array: list):
    left, right = 0, len(array) - 1
    while left != right-1:
        mid = (left + right) // 2
        if array[mid] > array[mid+1]:
            return mid+1
        if array[left] > array[mid]:
            right = mid
        else:
            left = mid
    return -1


def broken_search(nums: list, target: int) -> int:
    #  Your code
    #  “ヽ(´▽｀)ノ”

    # Добавил это так как не охота голову ломать
    # с поддержкой маленьких списков и бинарного поиска
    # ¯\_(ツ)_/¯
    if len(nums) < 3:
        if target in nums:
            return nums.index(target)
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

# 65136101

def in_put(string: str = None, to_int: bool = True):
    def str_or_arr(st: str):
        st = st.split(' ')
        if len(st) > 1:
            if to_int:
                return list(map(lambda x: int(x), st))
            return st
        return int(st[0])
    if string:
        return str_or_arr(string)
    return str_or_arr(input())


def broken_search(arr, target) -> int:
    """Бинарный поиск"""
    if not arr:
        return -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[left]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == '__main__':
    elements = in_put()
    target = in_put()
    arr = in_put()
    print(broken_search(arr, target))

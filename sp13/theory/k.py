# 64786828


def merge(arr: list, i_left: int, mid: int, i_right: int) -> list:
    # Your code
    # “ヽ(´▽｀)ノ”
    left = arr[i_left: mid]
    right = arr[mid: i_right]
    l, r, k = 0, 0, i_left
    while i_left + l < mid and mid + r < i_right:
        if left[l] <= right[r]:
            arr[k] = left[l]
            l += 1
        else:
            arr[k] = right[r]
            r += 1
        k += 1
    while i_left + l < mid:
        arr[k] = left[l]
        l += 1
        k += 1
    while mid + r < i_right:
        arr[k] = right[r]
        r += 1
        k += 1
    return arr


def merge_sort(arr: list, left: int, right: int) -> None:
    # Your code
    # “ヽ(´▽｀)ノ”
    if right - left > 1:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        arr[left: right] = merge(arr, left, mid, right)[left: right]

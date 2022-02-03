# 64787494

def in_put(string: str = None):
    def str_or_inputs(st: str):
        st = st.split(' ')
        if len(st) > 1:
            return list(map(lambda x: int(x), st))
        return int(st[0])
    if string:
        return str_or_inputs(string)
    return str_or_inputs(input())


def binary_search(arr, x, left, right):
    if x > arr[-1]:
        return -1
    mid = (left + right) // 2
    if arr[mid] < x:
        return binary_search(arr, x, mid + 1, right)
    elif arr[mid] >= x:
        if arr[mid - 1] >= x and mid > left:
            return binary_search(arr, x, left, mid)
    return mid + 1


def main():

    n = int(input())
    money = list(map(int, input().strip().split()))
    price = int(input())

    # n = in_put()
    # money = in_put()
    # price = in_put()

    # n = in_put('6')
    # money = in_put('1 2 4 4 6 8')
    # price = in_put('3')

    index = binary_search(money, price, left=0, right=n - 1)
    index2 = binary_search(
        money, price * 2, left=index, right=n - 1)
    print(index, index2)


if __name__ == "__main__":
    main()

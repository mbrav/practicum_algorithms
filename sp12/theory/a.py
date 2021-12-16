# 59827167

def in_put():
    x = int(input())
    y = int(input())
    arr = []
    for i in range(x):
        arr.extend(list(map(int, input().split())))
    return x, y, arr


def neo_matrix(x, y, arr):
    result = [0] * len(arr)
    for i in range(len(arr)):
        i_x = i % x
        i_y = i // x
        cur_i = i_x + i_y*x
        new_i = i_y + i_x*y
        result[new_i] = arr[cur_i]

    string = ""
    for i, val in enumerate(result):
        string += f"{val} "
        if i % y == y-1:
            string += "\n"
    return string


if __name__ == "__main__":
    y, x, arr = in_put()
    print(neo_matrix(x, y, arr))

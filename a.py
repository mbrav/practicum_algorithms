def in_put():
    x = int(input())
    y = list(map(int, input().split()))
    return x, y


def bad_realtor(arr):
    result = []
    plots = []
    val = 0
    # Пройдемся с начала улицы до конца улицы
    for i in range(len(arr)):
        if arr[i] == 0:
            val = 0
            plots.append(i)
        else:
            val += 1
        result.append(val)
    # Пройдемся с конца улицы до начала улицы
    for i in reversed(range(1, len(arr))):
        # Делаем корректировки
        if (result[i-1] - result[i] > 1
                or i < plots[0]):
            result[i-1] = result[i] + 1

    return " ".join(list(map(str, result)))


n, arr = in_put()
print(bad_realtor(arr))

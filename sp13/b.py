# nnnnnn


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


def in_put_users(ins: int, arr: list = None):
    users = []
    if arr:
        ins = len(arr)
    for i in range(ins):
        inputs = []
        if arr:
            inputs = in_put(arr[i], to_int=False)
        else:
            inputs = in_put(to_int=False)
        new_user = User(inputs[0], int(inputs[1]), int(inputs[2]))
        users.append(new_user)
    return users


class User:
    "Класс участника"

    def __init__(self, name, points, penalty):
        self.name = name
        self.points = points
        self.penalty = penalty

    def __str__(self):
        return f'#{self.id}\t{self.username}\t{self.tasks}\t-{self.penalty}'

    def __str__(self) -> str:
        return self.name

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def in_put_multi(ins: int):
    users = []
    for i in range(int(ins)):
        strings = input().split(' ')
        new_part = User(
            id=i,
            username=str(strings[0]),
            tasks=int(strings[1]),
            penalty=int(strings[2])
        )
        users.append(new_part)
    return users

if __name__ == '__main__':
    participants = in_put('5')

    inputs = [
        'alla 4 100',
        'gena 6 1000',
        'gosha 2 90',
        'rita 2 90',
        'timofey 4 80',
    ]

    users = in_put_users(participants, inputs)

    quick_sort(users, 0, participants-1)
    print(*users[::-1], sep='\n')

# nnnnnn

class User():
    "Класс участника"

    def __init__(self, id: int, username: str, tasks: int, penalty: int):
        self.id = id
        self.username = username
        self.tasks = tasks
        self.penalty = penalty

    def __str__(self):
        return f'#{self.id}\t{self.username}\t{self.tasks}\t-{self.penalty}'


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


def main(inputs: list):
    for i in inputs:
        print(i)


if __name__ == '__main__':
    num = int(input())
    users = in_put_multi(num)
    result = main(users)

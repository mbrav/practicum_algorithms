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


def quicksort(arr: list):
    if len(arr) < 2:
        return arr
    low, same, high = [], [], []
    pivot = arr[randint(0, len(arr) - 1)]
    for item in arr:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quicksort(low) + same + quicksort(high)


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

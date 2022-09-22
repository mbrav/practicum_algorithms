# 65136346


class User:
    "Класс участника"

    def __init__(self, name, score, penalty):
        self.name = name
        self.score = score
        self.penalty = penalty

    def __lt__(self, compare):
        if self.score != compare.score:
            return self.score < compare.score
        if self.penalty != compare.penalty:
            return self.penalty > compare.penalty
        return self.name > compare.name

    def __str__(self) -> str:
        return self.name


def quick_sort(array, start, end):
    def _sort(start, end):
        pivot = start
        for i in range(start+1, end+1):
            if (array[i] < array[start] or array[i] == array[start]):
                pivot += 1
                array[i], array[pivot] = array[pivot], array[i]
        array[pivot], array[start] = array[start], array[pivot]
        return pivot

    if start < end:
        pivot = _sort(start, end)
        quick_sort(array, start, pivot-1)
        quick_sort(array, pivot+1, end)


if __name__ == '__main__':
    participants = int(input())
    users = []
    for i in range(participants):
        name, score, penalty = input().split()
        users.append(User(name, int(score), int(penalty)))
    quick_sort(users, 0, participants-1)
    print(*users[::-1], sep='\n')

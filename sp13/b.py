# 65091587


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
    participants = in_put()

    users = in_put_users(participants)

    quick_sort(users, 0, participants-1)
    print(*users[::-1], sep='\n')

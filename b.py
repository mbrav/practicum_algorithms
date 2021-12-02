from collections import Counter


def in_put():
    x = int(input())
    string = (input()+input()+input()+input())
    y = []
    for i in string:
        if i != '.':
            y.append(int(i))
        else:
            y.append(i)
    return x, y


def game_sim(key, arr):
    result = []
    for i, v in Counter(arr).items():
        if v <= key*2:
            result.append(i)
    score = 0
    for i in range(1, 10):
        for k, value in Counter(arr).items():
            if i == k and value <= key*2:
                score += 1
    return score


n, arr = in_put()
print(game_sim(n, arr))

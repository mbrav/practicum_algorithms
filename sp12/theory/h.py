# nnnnnnn

def braket(code):
    a = ['[', '{', '(']
    b = [']', '}', ')']

    stack = []
    for i in code:
        if i in a:
            stack.append(i)
        elif i in b:
            pos = b.index(i)
            if (len(stack) > 0) and (a[pos] == stack[len(stack) - 1]):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # print(braket('(({})({[]}[])'))
    print(braket(input()))

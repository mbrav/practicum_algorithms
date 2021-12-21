# 62280912

from typing import List, Union

Number = Union[int, float]

t9 = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def in_put(string: str = None) -> List:
    if string:
        return [int(char) for char in string]
    return [int(char) for char in input()]


def t9_keypad(input, combinations, index, result=''):
    if index == -1:
        combinations.append(result)
        return result

    digit = input[index]

    for i in range(len(t9[digit])):
        t9_keypad(input, combinations, index - 1, t9[digit][i] + result)


def t9_keypad_it(input, index):
    def run(input, index, result=''):
        if index == -1:
            # yield from result
            return result
        if index > 0:
            digit = input[index]
            for i in range(len(t9[digit])):
                yield from run(input, index - 1, t9[digit][i] + result)
    yield from run(input, index)


def main(input: str = None):
    if not input:
        input = in_put('3456344535')
    combinations = []
    t9_keypad(input, combinations, len(input)-1)

    # # iterator try
    # result = t9_keypad_it(input, len(input)-1)
    # for res in result:
    #     print(res)

    return ' '.join(sorted(combinations))


if __name__ == '__main__':
    input = in_put()
    print(main(input))

import cProfile
import random

from a import main as a_main
from b import main as b_main


def repeater(func, repeat: int):
    for r in range(repeat):
        func()


def rand_int_arr(nums: int) -> list[int]:
    arr = []
    for i in range(nums):
        arr.append(random.randint(0, 100))
    return arr


# cProfile.run('a_main()')
# cProfile.run('b.main()')

cProfile.run('repeater(a_main, 1000)')
# cProfile.run('repeater(b.main, 1000)')

import cProfile
import functools
import random
import time

from a import broken_search
from tests import in_put


def timer(func):
    """Timer Decorator for measuring execution performance

    Args:
        none

    Returns:
        value
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()

        value = func(*args, **kwargs)

        run_time = time.perf_counter() - start_time

        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")

        return value
    return wrapper_timer


@timer
def repeater(func, repeat: int, *args, **kwargs):
    for r in range(repeat):
        func(*args, **kwargs)


def int_arr(nums: int, begin: int = 0):
    arr = []
    for i in range(begin, begin + nums):
        arr.append(i)
    return arr


def rand_int_arr(nums: int):
    arr = []
    for i in range(nums):
        arr.append(random.randint(0, 100))
    return arr


file = open('sp13/data/a_19.txt', 'r')
lines = file.read().split('\n')
bad_array = in_put(lines[2])
target = lines[1]
cProfile.run('broken_search(bad_array, target)')

# repeater(broken_search, 10000, bad_array, target)

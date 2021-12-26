import cProfile
import functools
import random
import time

from a import broken_search


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

        if run_time < 0.01:
            fraction = 1/run_time
            print(
                f"Finished {func.__name__!r} in 1/{fraction:.1f} fraction of a second!")
        else:
            print(f"Finished {func.__name__!r} in {run_time:.2f} secs")

        return value
    return wrapper_timer


def repeater(func, repeat: int):
    for r in range(repeat):
        func()


def int_arr(nums: int, begin: int = 0) -> list[int]:
    arr = []
    for i in range(begin, begin + nums):
        arr.append(i)
    return arr


def rand_int_arr(nums: int) -> list[int]:
    arr = []
    for i in range(nums):
        arr.append(random.randint(0, 100))
    return arr


bad_array = int_arr(174713, 300000) + int_arr(100000)
# target = bad_array[random.randint(0, len(bad_array))]
target = bad_array[193456]
cProfile.run('broken_search(bad_array, target)')
print(broken_search(bad_array, target))

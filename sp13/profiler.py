import cProfile
import functools
import random
import time

from a import main as a_main
from b import main as b_main


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


def rand_int_arr(nums: int) -> list[int]:
    arr = []
    for i in range(nums):
        arr.append(random.randint(0, 100))
    return arr


# cProfile.run('a_main()')
# cProfile.run('b.main()')

cProfile.run('repeater(a_main, 1000)')
# cProfile.run('repeater(b.main, 1000)')

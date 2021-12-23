import cProfile
import random

import a
import b
import c
import d
import e
import f
import g
import h
import i
import k


def repeater(func, repeat: int):
    for r in range(repeat):
        func()


def rand_int_arr(nums: int) -> list[int]:
    arr = []
    for i in range(nums):
        arr.append(random.randint(0, 1000))
    return arr

# cProfile.run('a.main()')
# cProfile.run('b.main()')
# cProfile.run('c.main()')
# cProfile.run('d.main()')
# cProfile.run('e.main()')
# cProfile.run('f.main()')
# cProfile.run('g.main()')
# cProfile.run('h.main()')
# cProfile.run('i.main()')
# cProfile.run('k.test()')


# cProfile.run('repeater(f.main, 1000)')
# cProfile.run('repeater(g.main, 1000)')
# cProfile.run('repeater(h.main, 1000)')
# cProfile.run('repeater(i.main, 1000)')
# cProfile.run('repeater(k.test, 1000)')

arrs = rand_int_arr(1000)
print(arrs)

cProfile.run('rand_int_arr(10000)')
# repeater(rand_int_arr(100), 10)

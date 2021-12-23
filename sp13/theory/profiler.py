import cProfile

import a
import b
import c
import d
import e
import f
import g
import h

# cProfile.run('a.main()')
# cProfile.run('b.main()')
# cProfile.run('c.main()')
# cProfile.run('d.main()')
# cProfile.run('e.main()')
# cProfile.run('f.main()')
# cProfile.run('g.main()')
# cProfile.run('h.main()')


def repeater(func, repeat: int):
    for r in range(repeat):
        func()


# cProfile.run('repeater(f.main, 1000)')
cProfile.run('repeater(g.main, 1000)')
# cProfile.run('repeater(h.main, 10000)')

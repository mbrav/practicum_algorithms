import unittest

import a
import b


class TestA(unittest.TestCase):

    def test_1(self):
        inputs = a.in_put('19 21 100 101 1 4 5 7 12')
        x = a.in_put('5')
        result = a.broken_search(inputs, x)
        assert result == int('6')

    def test_2(self):
        inputs = a.in_put('5 1')
        x = a.in_put('1')
        result = a.broken_search(inputs, x)
        assert result == int('1')

    def test_3(self):
        inputs = a.in_put('6 7 10 0 2 4 5')
        x = a.in_put('3')
        result = a.broken_search(inputs, x)
        assert result == int('-1')

    def test_4(self):
        inputs = a.in_put('8 10 0 2 4')
        x = a.in_put('4')
        result = a.broken_search(inputs, x)
        assert result == int('4')

    def test_5(self):
        inputs = a.in_put('5 1')
        x = a.in_put('1')
        result = a.broken_search(inputs, x)
        assert result == int('1')

    def test_6(self):
        inputs = a.in_put('2472 2473 2486 2534 2628 2977 3016 3155 3215 3383 3522 3533 3572 3599 3754 3856 3888 3890 4082 4130 4155 4207 4555 4556 4594 4597 4854 4861 4948 5085 5107 5251 5257 5378 5408 5452 5484 5584 5626 5701 5760 5781 5851 5855 6025 6047 6133 6243 6296 6314 6409 6516 6521 6659 6735 6813 6917 7059 7120 7296 7310 7345 7360 7379 7425 7498 7693 7925 7993 8035 8165 8277 8310 8363 8544 8562 8774 8827 8860 8952 9163 9177 9255 9793 9894 199 213 227 429 465 498 728 939 1502 1744 1768 1821 2317 2428 2471')
        x = a.in_put('227')
        result = a.broken_search(inputs, x)
        assert result == int('87')

    def test_7(self):
        inputs = a.in_put('5 1')
        x = a.in_put('1')
        result = a.broken_search(inputs, x)
        assert result == int('1')


# class TestB(unittest.TestCase):

#     def test_1(self):
#         inputs = b.in_put('2 5 - 4 /')
#         result = b.run(inputs)
#         assert result == int('-1')


if __name__ == '__main__':
    unittest.main()

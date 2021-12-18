import unittest

import b


class TestB(unittest.TestCase):

    def test_one(self):
        inputs = b.in_put('2 5 - 4 /')
        result = b.run(inputs)
        assert result == int('-1')

    def test_two(self):
        inputs = b.in_put('4 13 5 / +')
        result = b.run(inputs)
        assert result == int('6')

    def test_three(self):
        inputs = b.in_put('2 4 + 4 6 + *')
        result = b.run(inputs)
        assert result == int('60')

    def test_four(self):
        inputs = b.in_put('-4 -5 +')
        result = b.run(inputs)
        assert result == int('-9')


if __name__ == '__main__':
    unittest.main()

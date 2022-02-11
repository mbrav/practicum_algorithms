import unittest

import a
import b
from b import in_put, in_put_users


class TestA(unittest.TestCase):
    import a

    def test_1(self):
        inputs = in_put('19 21 100 101 1 4 5 7 12')
        x = in_put('5')
        result = a.broken_search(inputs, x)
        assert result == int('6')

    def test_2(self):
        inputs = in_put('5 1')
        x = in_put('1')
        result = a.broken_search(inputs, x)
        assert result == int('1')

    def test_3(self):
        inputs = in_put('2472 2473 2486 2534 2628 2977 3016 3155 3215 3383 3522 3533 3572 3599 3754 3856 3888 3890 4082 4130 4155 4207 4555 4556 4594 4597 4854 4861 4948 5085 5107 5251 5257 5378 5408 5452 5484 5584 5626 5701 5760 5781 5851 5855 6025 6047 6133 6243 6296 6314 6409 6516 6521 6659 6735 6813 6917 7059 7120 7296 7310 7345 7360 7379 7425 7498 7693 7925 7993 8035 8165 8277 8310 8363 8544 8562 8774 8827 8860 8952 9163 9177 9255 9793 9894 199 213 227 429 465 498 728 939 1502 1744 1768 1821 2317 2428 2471')
        x = in_put('227')
        result = a.broken_search(inputs, x)
        assert result == int('87')

    def test_4(self):
        inputs = in_put('6 7 10 0 2 4 5')
        x = in_put('3')
        result = a.broken_search(inputs, x)
        assert result == int('-1')

    def test_5(self):
        inputs = in_put('8 10 0 2 4')
        x = in_put('4')
        result = a.broken_search(inputs, x)
        assert result == int('4')

    def test_6(self):
        inputs = in_put('3271 3298 3331 3397 3407 3524 3584 3632 3734 3797 3942 4000 4180 4437 4464 4481 4525 4608 4645 4803 4804 4884 4931 4965 5017 5391 5453 5472 5671 5681 5959 6045 6058 6301 6529 6621 6961 7219 7291 7372 7425 7517 7600 7731 7827 7844 7987 8158 8169 8265 8353 8519 8551 8588 8635 9209 9301 9308 9336 9375 9422 9586 9620 9752 9776 9845 9906 9918 16 25 45 152 199 309 423 614 644 678 681 725 825 830 936 1110 1333 1413 1617 1895 1938 2107 2144 2184 2490 2517 2769 2897 2970 3023 3112 3156')
        x = in_put('25')
        result = a.broken_search(inputs, x)
        assert result == int('69')

    def test_7(self):
        inputs = in_put('8158 8164 8228 8296 8394 8426 8719 8728 9182 9220 9388 9453 9512 9544 9962 37 265 392 444 519 549 649 910 999 1056 1090 1211 1429 1526 1628 1688 1694 1733 1816 1994 2039 2290 2335 2389 2667 2690 2748 2799 2831 2905 2927 2993 3033 3048 3132 3166 3330 3346 3417 3457 3505 3573 3599 3679 3691 3839 4009 4013 4151 4192 4219 4305 4548 4799 4862 4866 4869 4976 5190 5401 5452 5477 5553 5938 5945 6041 6099 6132 6163 6437 6524 6780 6801 6888 7101 7187 7220 7228 7346 7387 7546 7762 7981 7983 8120')
        x = in_put('9220')
        result = a.broken_search(inputs, x)
        assert result == int('9')

    def test_8(self):
        inputs = in_put('1 2 3 4 5 6 7 8 9 10 11 12')
        x = in_put('10')
        result = a.broken_search(inputs, x)
        assert result == int('9')

    def test_file_19(self):
        file = open('sp13/data/a_19.txt', 'r')
        lines = file.read().split('\n')
        inputs = in_put(lines[2])
        x = lines[1]
        result = a.broken_search(inputs, x)
        assert result == int('2481')
        file.close()


class TestB(unittest.TestCase):

    def test_1(self):
        participants = in_put('5')
        inputs = [
            'alla 4 100',
            'gena 6 1000',
            'gosha 2 90',
            'rita 2 90',
            'timofey 4 80',
        ]
        result = ['gena', 'timofey', 'alla', 'gosha', 'rita']

        users = in_put_users(participants, inputs)
        b.quick_sort(users, 0, participants-1)

        for u, user in enumerate(users[::-1]):
            assert user.name == result[u]

    def test_2(self):
        participants = in_put('5')
        inputs = [
            'alla 0 10',
            'gena 0 9',
            'gosha 0 8',
            'rita 0 7',
            'timofey 0 0',
        ]
        result = ['timofey', 'rita', 'gosha', 'gena', 'alla']

        users = in_put_users(participants, inputs)
        b.quick_sort(users, 0, participants-1)

        for u, user in enumerate(users[::-1]):
            assert user.name == result[u]

    def test_3(self):
        participants = in_put('5')
        inputs = [
            'alla 0 0',
            'gena 1 0',
            'gosha 2 0',
            'rita 3 0',
            'timofey 4 0',
        ]
        result = ['timofey', 'rita', 'gosha', 'gena', 'alla']

        users = in_put_users(participants, inputs)
        b.quick_sort(users, 0, participants-1)

        for u, user in enumerate(users[::-1]):
            assert user.name == result[u]

    def test_4(self):
        participants = in_put('13')
        inputs = [
            'tufhdbi 76 58',
            'rqyoazgbmv 59 78',
            'qvgtrlkmyrm 35 27',
            'tgcytmfpj 70 27',
            'xvf 84 19',
            'jzpnpgpcqbsmczrgvsu 30 3',
            'evjphqnevjqakze 92 15',
            'wwzwv 87 8',
            'tfpiqpwmkkduhcupp 1 82',
            'tzamkyqadmybky 5 81',
            'amotrxgba 0 6',
            'easfsifbzkfezn 100 28',
            'kivdiy 70 47',
        ]
        result = [
            'easfsifbzkfezn',
            'evjphqnevjqakze',
            'wwzwv',
            'xvf',
            'tufhdbi',
            'tgcytmfpj',
            'kivdiy',
            'rqyoazgbmv',
            'qvgtrlkmyrm',
            'jzpnpgpcqbsmczrgvsu',
            'tzamkyqadmybky',
            'tfpiqpwmkkduhcupp',
            'amotrxgba',
        ]

        users = in_put_users(participants, inputs)
        b.quick_sort(users, 0, participants-1)

        for u, user in enumerate(users[::-1]):
            assert user.name == result[u]


if __name__ == '__main__':
    unittest.main()

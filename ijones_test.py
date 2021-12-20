import unittest

from ijones import IJones


class TestTarjanAlgorithm(unittest.TestCase):
    def test_ijones(self):
        arr = [['a', 'a', 'a', ],
               ['c', 'a', 'b', ],
               ['d', 'e', 'f', ]]

        alg = IJones(arr, 3, 3)

        self.assertEqual(alg.algo(), 5)

    def test_ijones_1(self):
        arr = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]

        alg = IJones(arr, 10, 1)

        self.assertEqual(alg.algo(), 2)

    def test_ijones_2(self):
        arr = [['a', 'a', 'a', 'a', 'a', 'a', 'a'],
               ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
               ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
               ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
               ['a', 'a', 'a', 'a', 'a', 'a', 'a'],
               ['a', 'a', 'a', 'a', 'a', 'a', 'a']]

        alg = IJones(arr, 7, 6)

        self.assertEqual(alg.algo(), 201684)

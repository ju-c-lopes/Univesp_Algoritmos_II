"""
from func import soma, mult


def test_soma():
    assert soma([1, 2, 3]) == 6, "Deve ser 6"


def test_mult():
    assert mult((2, 3, 4)) == 24, "Deve ser 24"


if __name__ == "__main__":
    test_soma()
    test_mult()
    print("Tudo ok!")
"""

import unittest
from func import soma, mult


class TestSum(unittest.TestCase):
    def test_sum1(self):
        self.assertEqual(soma([1, 2, 3]), 6, "Deve ser 6")

    def test_sum2(self):
        self.assertEqual(mult((2, 3, 4)), 24, "Deve ser 24")


if __name__ == "__main__":
    unittest.main()

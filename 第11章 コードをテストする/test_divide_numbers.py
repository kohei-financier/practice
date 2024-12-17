import unittest
from divide_numbers import divide_numbers

class TestDivideNumbers(unittest.TestCase):

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(6, 2), 3)

        # with構文を使って、例外をテストするという状況を作っておく
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)

if __name__ == '__main__':
    unittest.main()
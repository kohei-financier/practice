import unittest
from add_numbers import add_numbers

class AddNumbersTestCase(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(1, 2), 3)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
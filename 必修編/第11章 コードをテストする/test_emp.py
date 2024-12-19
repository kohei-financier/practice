import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.shimizu = Employee('shimizu', 'kohei', 60000000)
    
    def test_give_default_raise(self):
        # デフォルトで昇給が動くか確認する
        self.shimizu.give_raise()
        self.assertEqual(self.shimizu.salary, 60500000)
    
    def test_give_custom_raise(self):
        self.shimizu.give_raise(60000000)
        self.assertEqual(self.shimizu.salary, 120000000)

if __name__ == '__main__':
    unittest.main()

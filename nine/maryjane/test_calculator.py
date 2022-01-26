import unittest
from nine.maryjane import calculator


class MyTestCase(unittest.TestCase):

    def test_something(self):
        result = calculator.addition(9, 4)
        self.assertEqual(result, 13)  # add assertion here

    def test_subtraction(self):
        result = calculator.subtraction(3, 9)
        self.assertEqual(result, -6)


if __name__ == '__main__':
    unittest.main()

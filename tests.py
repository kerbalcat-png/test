import unittest
from main import divide,multiply

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(10,2),20)


class TestDivide(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide(6,2),3)

    def test_divide_2(self):
        self.assertEqual(divide("a",-1),TypeError)


def add2(num1):
    return num1+2


if __name__ == "__main__":
    unittest.main()

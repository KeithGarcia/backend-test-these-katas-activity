import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(10, 5), 15)
        self.assertEqual(katas.add(-1, 1), 0)
        self.assertEqual(katas.add(-1, -1), -2)

    def test_multiply(self):
        self.assertEqual(katas.multiply(10, 5), 50)
        self.assertEqual(katas.multiply(-1, 1), -1)
        self.assertEqual(katas.multiply(-1, -1), 1)

    def test_power(self):
        self.assertEqual(katas.power(2, 3), 8)
        self.assertEqual(katas.power(-4, 3), -64)

    def test_factorial(self):
        self.assertEqual(katas.factorial(4), 24)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(1), 0)
        self.assertEqual(katas.fibonacci(8), 13)


if __name__ == '__main__':
    unittest.main()

import unittest
from calculator import errechne_summe


class TestCalculatorFunctions(unittest.TestCase):

    def test_errechne_summe(self):
        self.assertEqual(errechne_summe(2, 3), 5)
        self.assertEqual(errechne_summe(-1, 1), 0)
        self.assertEqual(errechne_summe(-1, -1), -2)


if __name__ == '__main__':
    unittest.main()
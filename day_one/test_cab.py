import unittest
from taxicab import *


class TaxiCabTestCase(unittest.TestCase):

    def stest_parse(self):
        expected = ["R2", "L3"]
        result = parse("R2, L3")
        self.assertEqual(expected, result)

        expected = ["R5", "L5", "R5", "R3"]
        result = parse("R5, L5, R5, R3")
        self.assertEqual(expected, result)

    def stest_travel(self):
        self.assertEqual(travel(parse("R2, L3")), 5)
        self.assertEqual(travel(parse("R2, R2, R2")), 2)
        self.assertEqual(travel(parse("R5, L5, R5, R3")), 12)

    def test_travel(self):
        self.assertEqual(travel(parse("R8, R4, R4, R8")), 4)


if __name__ == '__main__':
    unittest.main()

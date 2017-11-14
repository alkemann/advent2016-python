import unittest
from bathroom import decode, decode_two


class MyTestCase(unittest.TestCase):
    def test_decode(self):
        self.assertEqual("1985", decode("ULL\nRRDDD\nLURDL\nUUUUD".split("\n")))

    def test_decode_two(self):
        self.assertEqual("5DB3", decode_two("ULL\nRRDDD\nLURDL\nUUUUD".split("\n")))

if __name__ == '__main__':
    unittest.main()

import unittest
from day_six.signals import corrected, Char


# noinspection SpellCheckingInspection
class SignalsTestCase(unittest.TestCase):
    def test_popular(self):
        strings = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa",
                   "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"]
        expected = "easter"
        result = corrected(strings)
        self.assertEqual(expected, result)

    def test_least(self):
        strings = ["eedadn", "drvtee", "eandsr", "raavrd", "atevrs", "tsrnev", "sdttsa",
                   "rasrtv", "nssdts", "ntnada", "svetve", "tesnvt", "vntsnd", "vrdear", "dvrsen", "enarar"]
        expected = "advent"
        result = corrected(strings, False)
        self.assertEqual(expected, result)

    def test_char(self):
        c = Char()
        c.add('a')
        c.add('a')
        c.add('b')
        c.add('c')
        c.add('c')
        c.add('c')
        expected = 'c'
        result = c.popular()
        self.assertEqual(expected, result)

        c = Char()
        c.add('a')
        c.add('b')
        c.add('z')
        c.add('z')
        expected = 'z'
        result = c.popular()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

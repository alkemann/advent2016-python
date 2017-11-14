import unittest
from day_five.chess import *


class HackerTestCase(unittest.TestCase):
    def test_look_for_hashes(self):
        self.assertEqual("18f47a30", look_for_hashes("abc"))

    def test_look_for_hashes_two(self):
        self.assertEqual("05ace8e3", look_for_hashes_two("abc"))
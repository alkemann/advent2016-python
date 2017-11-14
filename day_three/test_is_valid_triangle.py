from unittest import TestCase
from triangles import *

class TestIs_valid_triangle(TestCase):
    def test_is_valid_triangle(self):
        self.assertFalse(is_valid_triangle("    5  10  25"))
        self.assertFalse(is_valid_triangle("    1  100  250"))
        self.assertTrue(is_valid_triangle("    1  100  25"))

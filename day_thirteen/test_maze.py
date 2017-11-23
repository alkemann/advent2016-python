from unittest import TestCase
from day_thirteen.maze import binary, is_wall, is_binary_wall


class TestMaze(TestCase):

    def test_binary(self):
        self.assertEqual('1111', binary(15))
        self.assertEqual('0', binary(0))
        self.assertEqual('1001', binary(9))
        self.assertEqual('10001', binary(17))

    def test_is_binary_wall(self):
        self.assertTrue(is_binary_wall('0001'))
        self.assertTrue(is_binary_wall('0111'))
        self.assertTrue(is_binary_wall('11111'))

        self.assertFalse(is_binary_wall('0'))
        self.assertFalse(is_binary_wall('11'))
        self.assertFalse(is_binary_wall('101'))
        self.assertFalse(is_binary_wall('010111'))

    def test_is_wall(self):
        f = 10
        self.assertTrue(is_wall(1, 0, f))
        self.assertTrue(is_wall(3, 0, f))
        self.assertTrue(is_wall(4, 0, f))

        self.assertFalse(is_wall(0, 0, f))
        self.assertFalse(is_wall(0, 1, f))
        self.assertFalse(is_wall(1, 1, f))

from unittest import TestCase
from day_nine.decompress import decompress, decompress_two


class TestDecompress(TestCase):
    def test_string_stuff(self):
        # m = (27x12)(20x12)(13x14)(7x10)(1x12)A
        m = (27*12)+(20*12)+(13*14)+(7*10)+(1*12)
        self.assertEqual(241920, m)
        s = "A(1x5)BC"
        self.assertEqual("B", s[6:7])

    def test_decompress(self):
        self.assertEqual("ADVENT", decompress("ADVENT"))
        self.assertEqual("ABBBBBC", decompress("A(1x5)BC"))
        self.assertEqual("XYZXYZXYZ", decompress("(3x3)XYZ"))
        self.assertEqual("ABCBCDEFEFG", decompress("A(2x2)BCD(2x2)EFG"))
        self.assertEqual("(1x3)A", decompress("(6x1)(1x3)A"))
        self.assertEqual("X(3x3)ABC(3x3)ABCY", decompress("X(8x2)(3x3)ABCY"))

    def test_decompress_two(self):
        self.assertEqual(6, decompress_two("ADVENT"))
        self.assertEqual(7, decompress_two("A(1x5)BC"))
        self.assertEqual(9, decompress_two("(3x3)XYZ"))
        self.assertEqual(21, decompress_two("X(8x2)(3x3)ABCY"))
        self.assertEqual(241920, decompress_two("(27x12)(20x12)(13x14)(7x10)(1x12)A"))
        self.assertEqual(445, decompress_two("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"))


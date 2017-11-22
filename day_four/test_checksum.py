from unittest import TestCase
from day_four.checksum import room_is_real, calc_checksum


class TestChecksum(TestCase):

    def stest_is_room_real(self):
        self.assertTrue(room_is_real("aaaaa-bbb-z-y-x", "abxyz"))
        self.assertTrue(room_is_real("a-b-c-d-e-f-g-h", "abcde"))
        self.assertTrue(room_is_real("not-a-real-room", "oarel"))
        self.assertFalse(room_is_real("totally-real-room", "decoy"))

    def test_checksum(self):
        self.assertEquals("abxyz", calc_checksum("aaaaa-bbb-z-y-x"))
        self.assertEquals("abcde", calc_checksum("a-b-c-d-e-f-g-h"))
        self.assertEquals("oarel", calc_checksum("not-a-real-room"))

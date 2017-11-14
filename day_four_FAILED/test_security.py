from unittest import TestCase

from day_four_FAILED.security import is_room_real, check_checksum


class TestSecurity(TestCase):
    def stest_is_room_real(self):
        self.assertTrue(is_room_real("aaaaa-bbb-z-y-x-123[abxyz]"))
        self.assertTrue(is_room_real("a-b-c-d-e-f-g-h-987[abcde]"))
        self.assertTrue(is_room_real("not-a-real-room-404[oarel]"))
        self.assertFalse(is_room_real("totally-real-room-200[decoy]"))

    def test_check_checksum(self):
        # self.assertTrue(check_checksum("aaaaa-bbb-z-y-x", "abxyz"))
        # self.assertTrue(check_checksum("a-b-c-d-e-f-g-h", "abcde"))
        self.assertTrue(check_checksum("not-a-real-room", "oarel"))
        self.assertFalse(check_checksum("totally-real-room", "decoy"))

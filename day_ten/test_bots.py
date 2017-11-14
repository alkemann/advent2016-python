from unittest import TestCase
from day_ten.bots import find_answer


class TestBots(TestCase):
    def test_find_answer(self):
        com = [
            "value 5 goes to bot 2",
            "bot 2 gives low to bot 1 and high to bot 0",
            "value 3 goes to bot 1",
            "bot 1 gives low to output 1 and high to bot 0",
            "bot 0 gives low to output 2 and high to output 0",
            "value 2 goes to bot 2"
        ]
        # Assert that bot 2 is the one that checks chips 5 and 2
        self.assertEqual(2, find_answer(com, 5, 3))

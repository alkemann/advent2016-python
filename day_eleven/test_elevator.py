from unittest import TestCase
from day_eleven.elevator import find_answer


class TestElevator(TestCase):
    def test_find_answer_given(self):
        instructions = [
            "The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.",
            "The second floor contains a hydrogen generator.",
            "The third floor contains a lithium generator.",
            "The fourth floor contains nothing relevant.",
        ]
        self.assertEqual(11, find_answer(instructions))

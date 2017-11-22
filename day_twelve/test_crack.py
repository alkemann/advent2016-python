from unittest import TestCase
from day_twelve.crack import apply_commands


class TestCrack(TestCase):
    def test_find_answer_given(self):
        instructions = [
            "cpy 41 a",
            "inc a",
            "inc a",
            "dec a",
            "jnz a 2",
            "dec a"
        ]
        result = apply_commands(instructions)
        self.assertEqual(42, result["a"])
        self.assertEqual(0, result["b"])
        self.assertEqual(0, result["c"])
        self.assertEqual(0, result["d"])

    def test_constructed(self):
        instructions = [
            "cpy 10 a",
            "inc a",
            "inc b",
            "inc b",
            "jnz 2 b",
            "inc a",
            "inc b",
            "inc a",
            "inc a",
        ]
        result = apply_commands(instructions)
        self.assertEqual(13, result["a"])
        self.assertEqual(3, result["b"])

    def test_go_back(self):
        instructions = [
            "cpy 10 a",
            "inc a",
            "cpy 3 b",
            "dec b",
            "inc a",
            "jnz b -2",
            "inc a",
        ]
        result = apply_commands(instructions)
        self.assertEqual(15, result["a"])
        self.assertEqual(0, result["b"])

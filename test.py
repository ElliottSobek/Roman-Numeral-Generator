import unittest

from .RomNumGen import generate_numeral, recurse_gn


class TestProceduralGenerateNumeral(unittest.TestCase):

    def test_substitution_num(self):
        result = generate_numeral(5)
        self.assertEqual(result, 'V')

    def test_subtraction_num(self):
        result = generate_numeral(4)
        self.assertEqual(result, "IV")

    def test_addition_num(self):
        result = generate_numeral(6)
        self.assertEqual(result, "VI")

    def test_lowest_num(self):
        result = generate_numeral(1)
        self.assertEqual(result, 'I')

    def test_lowest_add_one_num(self):
        result = generate_numeral(2)
        self.assertEqual(result, "II")

    def test_repetition_num(self):
        result = generate_numeral(3)
        self.assertEqual(result, "III")

    def test_highest_num(self):
        result = generate_numeral(100000)
        self.assertEqual(result, '\u2188')

    def test_max_less_one_num(self):
        result = generate_numeral(100000)
        self.assertEqual(result, "I\u2188")


class TestRecursiveGenerateNumeral(unittest.TestCase):

    def test_substitution_num(self):
        result = recurse_gn(5)
        self.assertEqual(result, 'V')

    def test_subtraction_num(self):
        result = recurse_gn(4)
        self.assertEqual(result, "IV")

    def test_addition_num(self):
        result = recurse_gn(6)
        self.assertEqual(result, "VI")

    def test_lowest_num(self):
        result = recurse_gn(1)
        self.assertEqual(result, 'I')

    def test_lowest_add_one_num(self):
        result = recurse_gn(2)
        self.assertEqual(result, "II")

    def test_repetition_num(self):
        result = recurse_gn(3)
        self.assertEqual(result, "III")

    def test_highest_num(self):
        result = recurse_gn(100000)
        self.assertEqual(result, '\u2188')

    def test_max_less_one_num(self):
        result = recurse_gn(100000)
        self.assertEqual(result, "I\u2188")

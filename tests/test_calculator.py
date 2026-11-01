import unittest

from calculator import add


class TestCalculator(unittest.TestCase):

    # Positive Testing

    def test_addition_positive_numbers(self):
        self.assertEqual(add(5, 3), 8)

    def test_addition_negative_numbers(self):
        self.assertEqual(add(-5, -3), -8)

    def test_addition_positive_and_negative(self):
        self.assertEqual(add(-5, 3), -2)

    def test_addition_with_zero(self):
        self.assertEqual(add(5, 0), 5)

    def test_addition_decimal_numbers(self):
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

    # Negative Testing

    def test_string_operand_raises_error(self):
        with self.assertRaises(TypeError):
            add("5", 2)

    def test_none_operand_raises_error(self):
        with self.assertRaises(TypeError):
            add(None, 2)

    def test_boolean_operand_raises_error(self):
        with self.assertRaises(TypeError):
            add(True, 2)


if __name__ == "__main__":
    unittest.main()
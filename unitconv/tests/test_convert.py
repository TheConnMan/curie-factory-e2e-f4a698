import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_kelvin_celsius(self):
        self.assertEqual(convert(273.15, "k", "c"), 0)
        self.assertEqual(convert(0, "c", "k"), 273.15)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert(32, "f", "k"), 273.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(convert(273.15, "k", "f"), 32.0)

    def test_kelvin_same_unit(self):
        self.assertEqual(convert(300, "k", "k"), 300)

    def test_kelvin_case_insensitive(self):
        self.assertEqual(convert(273.15, "K", "C"), 0)

    def test_below_absolute_zero_rejected(self):
        for args in [(-1, "k", "c"), (-1, "k", "k"), (-273.16, "c", "k"),
                     (-273.16, "c", "f"), (-459.68, "f", "c"),
                     (-459.68, "f", "k")]:
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    convert(*args)

    def test_absolute_zero_accepted(self):
        self.assertEqual(convert(0, "k", "k"), 0)
        self.assertAlmostEqual(convert(-273.15, "c", "f"), -459.67)
        self.assertEqual(convert(-459.67, "f", "f"), -459.67)
        convert(-459.67, "f", "k")

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

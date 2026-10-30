import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert(273.15, "k", "c"), 0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert(0, "c", "k"), 273.15)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert(32, "f", "k"), 273.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(convert(273.15, "k", "f"), 32.0)

    def test_kelvin_same_unit(self):
        self.assertEqual(convert(300, "k", "k"), 300)

    def test_kelvin_case_insensitive(self):
        self.assertAlmostEqual(convert(273.15, "K", "C"), 0)

    def test_below_absolute_zero_rejected(self):
        for value, unit in [(-1, "k"), (-273.16, "c"), (-459.68, "f")]:
            for dst in ("k", "c", "f"):
                with self.subTest(value=value, unit=unit, dst=dst):
                    with self.assertRaises(ValueError):
                        convert(value, unit, dst)

    def test_absolute_zero_accepted(self):
        self.assertAlmostEqual(convert(0, "k", "c"), -273.15)
        self.assertAlmostEqual(convert(-273.15, "c", "k"), 0)
        self.assertAlmostEqual(convert(-459.67, "f", "k"), 0)

    def test_length_negative_still_valid(self):
        self.assertAlmostEqual(convert(-1, "km", "m"), -1000.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

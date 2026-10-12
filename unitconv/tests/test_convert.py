import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_celsius_identity(self):
        self.assertEqual(convert(25, "c", "c"), 25)

    def test_fahrenheit_identity(self):
        self.assertEqual(convert(98.6, "f", "f"), 98.6)

    def test_length_identity(self):
        self.assertEqual(convert(5, "km", "km"), 5)
        self.assertEqual(convert(2, "m", "m"), 2)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert(100, "c", "k"), 373.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert(273.15, "k", "c"), 0.0)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert(212, "f", "k"), 373.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(convert(373.15, "k", "f"), 212.0)

    def test_kelvin_identity(self):
        self.assertEqual(convert(300, "k", "k"), 300)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

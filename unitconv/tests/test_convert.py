import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert(0, "c", "k"), 273.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert(273.15, "k", "c"), 0.0)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert(32, "f", "k"), 273.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(convert(273.15, "k", "f"), 32.0)

    def test_kelvin_identity(self):
        self.assertAlmostEqual(convert(300, "k", "k"), 300.0)

    def test_celsius_identity(self):
        self.assertAlmostEqual(convert(25, "c", "c"), 25.0)

    def test_fahrenheit_identity(self):
        self.assertAlmostEqual(convert(75, "f", "f"), 75.0)

    def test_length_identity(self):
        for src in ("m", "km", "mi", "ft"):
            self.assertAlmostEqual(convert(7, src, src), 7.0)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

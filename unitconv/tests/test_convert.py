import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_nmi_to_m_exact(self):
        self.assertEqual(convert(1, "nmi", "m"), 1852.0)

    def test_nmi_round_trip(self):
        for unit in ("m", "km", "mi", "ft"):
            self.assertAlmostEqual(convert(convert(1, "nmi", unit), unit, "nmi"), 1.0)

    def test_nmi_to_km_and_mi(self):
        self.assertAlmostEqual(convert(1, "nmi", "km"), 1.852, places=6)
        self.assertAlmostEqual(convert(1, "nmi", "mi"), 1852.0 / 1609.344, places=6)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

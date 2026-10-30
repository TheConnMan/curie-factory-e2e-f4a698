import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_mm_to_m(self):
        self.assertEqual(convert(1000, "mm", "m"), 1)

    def test_m_to_mm(self):
        self.assertAlmostEqual(convert(1, "m", "mm"), 1000.0)

    def test_mm_round_trip(self):
        self.assertAlmostEqual(convert(convert(37.5, "mm", "m"), "m", "mm"), 37.5)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

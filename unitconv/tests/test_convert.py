import unittest

from unitconv.convert import LENGTH_TO_METERS, UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")

    def test_nmi_defined_as_1852_meters(self):
        self.assertEqual(LENGTH_TO_METERS["nmi"], 1852.0)

    def test_nmi_roundtrip_all_length_units(self):
        for unit in LENGTH_TO_METERS:
            with self.subTest(unit=unit):
                self.assertAlmostEqual(
                    convert(1, "nmi", unit), 1852.0 / LENGTH_TO_METERS[unit]
                )
                self.assertAlmostEqual(convert(1, unit, "nmi"), LENGTH_TO_METERS[unit] / 1852.0)
                self.assertAlmostEqual(convert(convert(1, "nmi", unit), unit, "nmi"), 1.0)


if __name__ == "__main__":
    unittest.main()

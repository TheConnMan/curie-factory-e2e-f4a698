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

    def test_nmi_to_existing_units(self):
        self.assertAlmostEqual(convert(1, "nmi", "m"), 1852.0)
        self.assertAlmostEqual(convert(1, "nmi", "km"), 1.852, places=5)
        self.assertAlmostEqual(convert(1, "nmi", "mi"), 1.15078, places=5)
        self.assertAlmostEqual(convert(1, "nmi", "ft"), 6076.12, places=2)
        self.assertAlmostEqual(convert(1, "nmi", "nmi"), 1.0)

    def test_nmi_roundtrips(self):
        for unit in ("m", "km", "mi", "ft"):
            self.assertAlmostEqual(convert(convert(7, unit, "nmi"), "nmi", unit), 7.0)
            self.assertAlmostEqual(convert(convert(7, "nmi", unit), unit, "nmi"), 7.0)

    def test_nmi_3_5_meters_roundtrip(self):
        meters = convert(3.5, "nmi", "m")
        self.assertAlmostEqual(meters, 3.5 * 1852.0)
        self.assertAlmostEqual(convert(meters, "m", "nmi"), 3.5)

    def test_nmi_temperature_mix_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "nmi")


if __name__ == "__main__":
    unittest.main()

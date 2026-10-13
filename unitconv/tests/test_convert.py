import unittest

from unitconv.convert import LENGTH_TO_METERS, UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_nmi_to_m(self):
        self.assertAlmostEqual(convert(1, "nmi", "m"), 1852.0)

    def test_m_to_nmi(self):
        self.assertAlmostEqual(convert(1852, "m", "nmi"), 1.0)

    def test_nmi_to_km(self):
        self.assertAlmostEqual(convert(1, "nmi", "km"), 1.852)

    def test_nmi_to_mi(self):
        self.assertAlmostEqual(convert(1, "nmi", "mi"), 1.15078, places=4)

    def test_nmi_to_ft_round_trip(self):
        feet = convert(1, "nmi", "ft")
        self.assertAlmostEqual(convert(feet, "ft", "nmi"), 1.0)

    def test_nmi_converts_to_and_from_every_length_unit(self):
        for unit in LENGTH_TO_METERS:
            self.assertAlmostEqual(convert(2, "nmi", unit), 2 * LENGTH_TO_METERS["nmi"] / LENGTH_TO_METERS[unit])
            self.assertAlmostEqual(convert(2, unit, "nmi"), 2 * LENGTH_TO_METERS[unit] / LENGTH_TO_METERS["nmi"])

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

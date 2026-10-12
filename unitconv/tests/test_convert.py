import unittest

from unitconv.convert import UnknownUnit, convert


class ConvertTests(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "f", "c"), 0.0)

    def test_km_to_mi(self):
        self.assertAlmostEqual(convert(5, "km", "mi"), 3.10686, places=4)

    def test_nmi_to_km(self):
        self.assertAlmostEqual(convert(1, "nmi", "km"), 1.852)

    def test_km_to_nmi(self):
        self.assertAlmostEqual(convert(1, "km", "nmi"), 1 / 1.852)

    def test_nmi_to_mi(self):
        self.assertAlmostEqual(convert(1, "nmi", "mi"), 1852 / 1609.344)

    def test_nmi_to_ft(self):
        self.assertAlmostEqual(convert(1, "nmi", "ft"), 1852 / 0.3048)

    def test_m_to_nmi(self):
        self.assertAlmostEqual(convert(1852, "m", "nmi"), 1.0)

    def test_nmi_round_trip_every_length_unit(self):
        # 1 nmi must convert to and from every existing length unit.
        for unit in ("m", "km", "mi", "ft"):
            self.assertAlmostEqual(convert(convert(1, "nmi", unit), unit, "nmi"), 1.0)

    def test_nmi_round_trip_to_meters(self):
        # 3.5 nmi to meters and back must return the original value.
        meters = convert(3.5, "nmi", "m")
        self.assertAlmostEqual(meters, 3.5 * 1852)
        self.assertAlmostEqual(convert(meters, "m", "nmi"), 3.5)

    def test_unknown_unit(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "parsec", "m")

    def test_mixed_categories_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "c", "m")


if __name__ == "__main__":
    unittest.main()

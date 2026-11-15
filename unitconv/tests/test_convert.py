import unittest

from unitconv.convert import UnknownUnit, convert


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

    def test_meter_alias_source(self):
        self.assertAlmostEqual(convert(1, "meter", "ft"), convert(1, "m", "ft"))

    def test_metre_alias_destination_case_insensitive(self):
        self.assertAlmostEqual(convert(1, "ft", "METRE"), convert(1, "ft", "m"))

    def test_aliases_both_positions_mixed_case(self):
        self.assertAlmostEqual(
            convert(2, "Meter", "MeTrE"), convert(2, "m", "m")
        )

    def test_alias_mixed_with_temperature_rejected(self):
        with self.assertRaises(ValueError):
            convert(1, "meter", "c")

    def test_unknown_unit_still_rejected(self):
        with self.assertRaises(UnknownUnit):
            convert(1, "metres", "m")


if __name__ == "__main__":
    unittest.main()

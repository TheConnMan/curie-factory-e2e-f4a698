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

    def test_ftus_to_meters(self):
        self.assertAlmostEqual(convert(3937, "ftus", "m"), 1200.0)

    def test_meters_to_ftus(self):
        self.assertAlmostEqual(convert(1200, "m", "ftus"), 3937.0)

    def test_ftus_to_feet(self):
        self.assertAlmostEqual(convert(1, "ftus", "ft"), 1.000002, places=6)

    def test_ftus_round_trip_all_length_units(self):
        for unit in LENGTH_TO_METERS:
            if unit == "ftus":
                continue
            with self.subTest(unit=unit):
                converted = convert(1, "ftus", unit)
                back = convert(converted, unit, "ftus")
                self.assertAlmostEqual(back, 1.0)


if __name__ == "__main__":
    unittest.main()

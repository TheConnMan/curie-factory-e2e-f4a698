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

    def test_ftus_to_meters(self):
        self.assertAlmostEqual(convert(3937, "ftus", "m"), 1200.0)

    def test_ftus_to_feet(self):
        self.assertAlmostEqual(convert(1, "ftus", "ft"), 1.000002000004, places=9)

    def test_ftus_to_every_other_length_unit(self):
        expected = {
            "m": 0.3048006096012192,
            "km": 0.0003048006096012192,
            "mi": 0.00018939431818257576,
            "ft": 1.000002000004,
        }
        for unit, value in expected.items():
            self.assertAlmostEqual(convert(1, "ftus", unit), value, places=9)

    def test_every_other_length_unit_to_ftus(self):
        for unit in ("m", "km", "mi", "ft"):
            forward = convert(1, unit, "ftus")
            back = convert(forward, "ftus", unit)
            self.assertAlmostEqual(back, 1.0, places=9)


if __name__ == "__main__":
    unittest.main()

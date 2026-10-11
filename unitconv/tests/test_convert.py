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

    def test_nmi_to_m(self):
        """Test nautical miles to meters conversion."""
        self.assertAlmostEqual(convert(1, "nmi", "m"), 1852.0)

    def test_m_to_nmi(self):
        """Test meters to nautical miles conversion."""
        self.assertAlmostEqual(convert(1852, "m", "nmi"), 1.0)

    def test_nmi_to_km(self):
        """Test nautical miles to kilometers conversion."""
        self.assertAlmostEqual(convert(1, "nmi", "km"), 1.852)

    def test_nmi_to_mi(self):
        """Test nautical miles to statute miles conversion."""
        self.assertAlmostEqual(convert(1, "nmi", "mi"), 1.15078, places=4)

    def test_nmi_to_ft(self):
        """Test nautical miles to feet conversion."""
        self.assertAlmostEqual(convert(1, "nmi", "ft"), 6076.115, places=2)

    def test_nmi_round_trip(self):
        """Test round-trip conversions with nautical miles for all length units."""
        test_value = 2.5
        # Test round-trip conversion for each length unit
        for unit in ["m", "km", "mi", "ft"]:
            result = convert(convert(test_value, "nmi", unit), unit, "nmi")
            self.assertAlmostEqual(result, test_value, places=6,
                                   msg=f"Round-trip nmi -> {unit} -> nmi failed")

    def test_nmi_to_meters_round_trip(self):
        """Test round-trip conversion of 3.5 nautical miles to meters and back."""
        nautical_miles = 3.5
        meters = convert(nautical_miles, "nmi", "m")
        result = convert(meters, "m", "nmi")
        self.assertAlmostEqual(result, nautical_miles, places=6)


if __name__ == "__main__":
    unittest.main()

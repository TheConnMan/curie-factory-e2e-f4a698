import unittest

import triage_probe


class AddTests(unittest.TestCase):
    def test_reported_input(self):
        self.assertEqual(triage_probe.add(2, 3), 5)

    def test_negatives_and_zero(self):
        self.assertEqual(triage_probe.add(-1, 1), 0)
        self.assertEqual(triage_probe.add(0, 0), 0)
        self.assertEqual(triage_probe.add(10, 5), 15)


if __name__ == "__main__":
    unittest.main()

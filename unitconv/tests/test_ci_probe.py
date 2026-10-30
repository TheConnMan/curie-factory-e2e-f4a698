import unittest

from unitconv.ci_probe import ready


class CiProbeTests(unittest.TestCase):
    def test_ready_is_true(self):
        self.assertIs(ready(), True)


if __name__ == "__main__":
    unittest.main()

import unittest
from dayoftheweek import DayOfTheWeek


class TestDayOfTheWeek(unittest.TestCase):
    def test_init(self):
        d = DayOfTheWeek("F")
        self.assertEqual(d.name(), "Friday")
        d = DayOfTheWeek("Th")
        self.assertEqual(d.name(), "Thursday")


if __name__ == "__main__":
    unittest.main()

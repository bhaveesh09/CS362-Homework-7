from Programs import LeapYear
import unittest

class testLeapYear(unittest.TestCase):
    def test_leapYear(self):
        case = LeapYear(-2000)
        self.assertEqual(case, False)


if __name__ == '__main__':
    unittest.main()


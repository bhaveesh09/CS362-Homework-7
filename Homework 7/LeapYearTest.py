from Programs import LeapYear
import unittest

class testLeapYear(unittest.TestCase):
    def test_leapYear(self):
        case = LeapYear(-2000)
        self.assertEqual(case, False)
    def test_leapYear2(self):
        case = LeapYear(2000)
        self.assertEqual(case, True)
    def test_leapYear3(self):
        case = LeapYear(4000)
        self.assertEqual(case, True)



if __name__ == '__main__':
    unittest.main()


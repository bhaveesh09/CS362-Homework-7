from LeapYearProgram import leapYear
import unittest


class testLeapYear(unittest.TestCase):
    def test_leapYear(self):
        case = leapYear(-2000)
        self.assertEqual(case, False)




    if __name__ == '__main__':
        unittest.main()
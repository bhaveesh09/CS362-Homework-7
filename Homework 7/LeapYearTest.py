from Programs import FizzBuzz, LeapYear
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
    def test_leapYear4(self):
        case = LeapYear(2005)
        self.assertEqual(case, False)

class testFizzBuzz(unittest.TestCase):
    def test_FizzBuzz(self):
        for i in range(1,100,1):
            case = FizzBuzz()
            if (i%3==0 and i%5==0):
                self.assertEqual(case, "FizzBuzz")
            elif (i%3==0 and i%5!=0):
                self.assertEqual(case, "Fizz")
            elif (i%5==0 and i%3!=0):
                self.assertEqual(case, "Buzz")
            else:
                self.assertEqual(case, i)

if __name__ == '__main__':
    unittest.main()


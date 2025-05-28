import unittest
import calc


class TestCalc(unittest.TestCase):

    def test_add(self): # must start with "test_"
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self): # must start with "test_"
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)
    
    def test_multiply(self): # must start with "test_"
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self): # must start with "test_"
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)

        # self.assertRaises(ValueError, calc.divide, 10, 0) # exception we expect, function we want to test, pass in each argument we want to pass into the divide function speratley

        with self.assertRaises(ValueError): # same thing as above
            calc.divide(10,0)

    

if __name__ == '__main__': # allows you to run with 
    unittest.main()
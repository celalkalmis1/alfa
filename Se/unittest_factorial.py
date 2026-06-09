import unittest

def factorial(n):
    result = 1
    for i in range (1, n+1):
        result*=i
    return result
    
class FactorialTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(factorial(5), 120)
    def testcase2(self):
        self.assertLess(factorial(3),8)
    def testcase3(self):
        self.assertGreater(factorial(4),23)
        
unittest.main()
    

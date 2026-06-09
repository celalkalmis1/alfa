import unittest

def triangle_area(a ,h):
    return (a*h)/2
    
class TriangleAreaTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(triangle_area(1,2), 1)
    
    def testcase2(self):
        self.assertLess(triangle_area(5,4),11)
        
    def testcase3(self):
        self.assertGreater(triangle_area(5,12),22)
        
unittest.main()
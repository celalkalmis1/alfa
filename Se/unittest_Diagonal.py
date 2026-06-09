import unittest

def Diogonal(n):
    if n <= 3:
        return 0
    else:
        return (n*(n-3))/2
   
    
class DiogonalTest(unittest.TestCase):

    
    def test_1(self):
        self.assertEqual(Diogonal(1), 0)
    def test_2(self):
        self.assertEqual(Diogonal(2), 0)
    def test_3(self):
        self.assertEqual(Diogonal(3), 0)
    def test_4(self):
        self.assertEqual(Diogonal(6), 9)
    def test_5(self):
        self.assertEqual(Diogonal(9), 27)
    
    
        


if __name__ == '__main__':
    unittest.main()
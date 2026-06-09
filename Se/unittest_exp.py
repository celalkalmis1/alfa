import unittest


def power(base, exponent):
    return base ** exponent
    
class TestPower(unittest.TestCase):

    
    def test_1(self):
        self.assertEqual(power(1,0), 1)
    def test_2(self):
        self.assertLess(power(101,4), 1000000)
    def test_3(self):
        self.assertGreater(power(3,3), 22)
    def test_4(self):
        self.assertEqual(power(6,2), 36)
    def test_5(self):
        self.assertEqual(power(9,2), 81)
    
    
        


if __name__ == '__main__':
    unittest.main()
    
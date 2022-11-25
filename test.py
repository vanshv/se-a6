import unittest

from sum import summation

class TestSum(unittest.TestCase):
    def test1(self):
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 500)
        
    def test2(self):
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 50)
        
    def test2(self):
        data = [30, 20]
        result = summation(data)
        self.assertEqual(result, 50)
        
    def test2(self):
        data = [20, 0]
        result = summation(data)
        self.assertEqual(result, 0)
        
    def test2(self):
        data = [20, -20]
        result = summation(data)
        self.assertEqual(result, 0)
        

if __name__ == '__main__':
    unittest.main()

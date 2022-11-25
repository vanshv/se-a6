#!/usr/bin/python3

import unittest
from Code import summation

class TestSum(unittest.TestCase):
    def testp1(self):
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 50)
        
    def testp2(self):
        data = [30, 20]
        result = summation(data)
        self.assertEqual(result, 50)
        
    def testp3(self):
        data = [20, -20]
        result = summation(data)
        self.assertEqual(result, 0)
        

if __name__ == '__main__':
    unittest.main()
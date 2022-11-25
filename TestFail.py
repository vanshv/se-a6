#!/usr/bin/python3

import unittest
from Code import summation

class TestSum(unittest.TestCase):
    def testf1(self):
        data = [20, 30]
        result = summation(data)
        self.assertEqual(result, 500)

    def testf2(self):
        data = [20, 0]
        result = summation(data)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
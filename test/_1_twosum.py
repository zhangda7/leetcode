'''
Created on 2015/6/26

@author: dazhang
'''
import unittest
from solution import _1_twosum


class Test(unittest.TestCase):


    def testName(self):
        s = _1_twosum.Solution()
        self.assertEqual([1,2], s.twoSum([-1,-2,-3,-4,-5, -6, -9], -3), "fail")
        self.assertEqual([2,7], s.twoSum([-1,-2,-3,-4,-5, -6, -9], -11), "fail")
        self.assertEqual([6,7], s.twoSum([-1,-2,-3,-4,-5, -6, -9], -15), "fail")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
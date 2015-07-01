'''
Created on 2015/6/26

@author: dazhang
'''
import unittest
from solution import _3_lsc


class Test(unittest.TestCase):


    def testName(self):
        s = _3_lsc.Solution()
        self.assertEqual(3, s.lengthOfLongestSubstring("abcabc"), "fail")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
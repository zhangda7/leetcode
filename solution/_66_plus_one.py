# -*- coding:utf-8 -*-
'''
Created on 2015/7/26

@author: dazhang

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

'''

class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        if digits == None or len(digits) == 0:
            return digits
        length = len(digits)
        added = 1
        for i in range(len(digits) - 1, 0 , -1):
            digits[i] = digits[i] + added
            if digits[i] == 10:
                digits[i] = 0
                added = 1
            else:
                added = 0
                break
        if digits[0] == 9 and added == 1:
            ret = []
            ret.append(1)
            ret.append(0)
            ret.extend(digits[1:])
            return ret
        else:
            digits[0] += added
            return digits
        

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([9,9,9,9]))
    pass
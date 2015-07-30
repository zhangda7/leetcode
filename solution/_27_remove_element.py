# -*- coding:utf-8 -*-
'''
Created on 2015/7/25

@author: dazhang

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Solution:
remove in place, and only return the new length, so no more need shift, just use m and n
m indicate the position to be replaced
n indicate which element will replace n
so if nums[i] == val, just increase n, if nums[i] != val, just let nums[m] = nums[n] and increase m and n
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if nums == None or len(nums) == 0:
            return 0
        m = 0
        n = 0
        for i in range(len(nums)):
            if nums[i] == val:
                n += 1
            else:
                nums[m] = nums[n]
                m += 1
                n += 1
        print(nums)
        return m


if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([1,2,3,3,4,4,5], 3))
    pass
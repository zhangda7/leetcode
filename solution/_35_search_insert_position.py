# -*- coding:utf-8 -*-
'''
Created on 2015/7/31

@author: dazhang

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

Solution:
just still binary search.

'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        if nums == None or len(nums) == 0:
            return -1
        i = 0
        j = len(nums) - 1
        while(i <= j):
            index = (i + j) / 2
            if nums[index] == target:
                return index
            elif nums[index] < target:
                i = index + 1
            else:
                j = index - 1
        
        return i       
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6],7))
    pass
# -*- coding:utf-8 -*-
'''
Created on 2015/7/31

@author: dazhang

Search for a Range Total Accepted: 50461 Total Submissions: 184269 My Submissions Question Solution 
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        if nums == None or len(nums) == 0:
            return [-1, -1]
        i = 0
        j = len(nums) - 1
        index = 0
        found = False
        while(i <= j):
            index = (i + j) / 2
            #print i, j
            if nums[index] == target:
                found = True
                break
            elif nums[index] > target:
                j = index - 1
            else:
                i = index + 1
        #print(index)
        if found == False:
            return [-1, -1]
        else:
            start = index
            end = index
            while(start >= 0 and nums[start] == target):
                start -= 1
            start += 1
            while(end < len(nums) and nums[end] == target):
                end += 1
            end -= 1
        return [start, end]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 10))
    pass
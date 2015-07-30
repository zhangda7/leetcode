# -*- coding:utf-8 -*-
'''
Created on 2015/7/25

@author: dazhang

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.

Solution:
If can use extra space, this is very easy, just use a hashmap, can solve it easily and quickly.

Read the problem, sorted array, same with 27_remove_element, just be attention: use nums[m+1] = nums[i]
Because if 2 ele not equal, m + 1 = i, if 2 ele equal, m + 1 indicate the second euqal one, not the first, so we can replace.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        m = 0 
        n = 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[m]:
                continue
            else:
                nums[m + 1] = nums[i]
                m += 1
        print(nums)
        return m + 1
        
        
        

if __name__ == '__main__':
    s = Solution()
    #print(s.removeDuplicates([0,1,1,2,2,2,2,3,3]))
    print(s.removeDuplicates([0,1,2,3]))
    pass
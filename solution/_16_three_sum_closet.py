# -*- coding:utf-8 -*-
'''
Created on 2015/7/27

@author: dazhang

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Same with 3 sum. Easier
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        #print(nums)
        ret = 0
        previous = None
        subValue = 2**32
        for i in range(len(nums)):
            if previous == nums[i]:
                continue
            key = nums[i]
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                #print("%d %d %d" % (key, nums[start], nums[end]))
                sub = abs(target - (key + nums[start] + nums[end]))
                #print(sub)
                if sub < subValue:
                    subValue = sub
                    ret = key + nums[start] + nums[end]
                    
                if nums[start] + nums[end] + key > target:
                    end -= 1
                else:
                    start += 1
            #print(ret)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([0,2,1,-3], 1))
    pass
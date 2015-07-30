# -*- coding:utf-8 -*-
'''
Created on 2015年7月23日

@author: dazhang

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
'''
a[i] = max(a[i - 2] + n[i], a[i - 1])
This is true, do not think too much about it.
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        a = []
        for i in range(len(nums)):
            a.append(0)
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
        maxNum = 0
        for i in range(2,len(nums)):
            a[i] = max(a[i - 2] + nums[i], a[i - 1])
            if maxNum < a[i]:
                maxNum = a[i]
        #print(a)
        return maxNum

if __name__ == '__main__':
    s = Solution()
    print(s.rob([2,1,1,2]))
    pass
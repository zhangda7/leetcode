#-*- coding:utf-8 -*-
'''
Created on 2015/7/23

@author: dazhang

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

'''
just rob twice, with nums[0] and without nums[0]
'''
class Solution:
    def rob(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob1(nums[1:]), self.rob1(nums[:len(nums) - 1]))
    
    # @param {integer[]} nums
    # @return {integer}
    def rob1(self, nums):
        a = []
        for i in range(len(nums)):
            a.append(0)
        a[0] = nums[0]
        a[1] = max(nums[0], nums[1])
        maxNum = a[1]
        for i in range(2,len(nums)):
            a[i] = max(a[i - 2] + nums[i], a[i - 1])
            if maxNum < a[i]:
                maxNum = a[i]
        #print(a)
        return maxNum

if __name__ == '__main__':
    s = Solution()
    print(s.rob([]))
    print(s.rob([2]))
    print(s.rob([2,1]))
    print(s.rob([2,1,1,2]))
    print(s.rob([1,1,1]))
    print(s.rob([1,2,1,1]))
    print(s.rob([1,1,1,2]))
    pass
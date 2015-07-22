# -*- coding: utf-8 -*-  
'''
Created on 2015/7/22

@author: dazhang

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.

a[i] = max(n[i], a[i-1] + n[i])

'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        length = len(nums)
        ret = []
        for i in range(length):
            ret.append(0)
        ret[0] = nums[0]
        maxNum = ret[0]
        for i in range(1, length):
            ret[i] = max(nums[i], ret[i - 1] + nums[i])
            if ret[i] > maxNum:
                maxNum = ret[i]
        #print(ret)
        return maxNum
        

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    pass
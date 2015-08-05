# -*- coding:utf-8 -*-
'''
Created on 2015/7/31

@author: dazhang

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

首先我们找到中间节点mid，如果大于两边返回当前index就可以了，
如果左边的节点比mid大，那么我们可以继续在左半区间查找，这里面一定存在一个peak，为什么这么说呢？
假设此时的区间范围为[0, mid - 1]， 因为num[mid - 1]一定大于num[mid]了，如果num[mid - 2] <= num[mid - 1]，
那么num[mid - 1]就是一个peak。如果num[mid - 2] > num[mid - 1]，那么我们就继续在[0, mid - 2]区间查找，
因为num[-1]为负无穷，所以最终我们绝对能在左半区间找到一个peak。同理右半区间一样。

It's true.
'''

class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        if nums == None or len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0
        i = 0
        j = len(nums) - 1
        while(i <= j):
            mid = (i + j) / 2
            #print i,j,mid
            if (mid == 0 and nums[mid] > nums[mid + 1]):
                return mid
            
            elif (mid == len(nums) - 1 and nums[mid] > nums[mid - 1]):
                return mid
            elif (nums[mid] > nums[mid-1] and nums[mid] > nums[mid + 1]):
                return mid
                
            if mid > 0 and nums[mid-1] > nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        
        

if __name__ == '__main__':
    s = Solution()
    #print(s.findPeakElement([1,2,1,1,5,6]))
    print(s.findPeakElement([1,2]))
    pass
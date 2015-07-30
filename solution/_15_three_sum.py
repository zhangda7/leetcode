# -*- coding:utf-8 -*-
'''
Created on 2015/7/27

@author: dazhang

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
    
Solution:
1.sort this array
2.locate one element i, then use 2 pointer start and end, if n[i] * -1 == n[start] + n[end], save, then if n[i] * -1 > n[start] + n[end], start++,
then end--

a little complcated 

Do not forget to elimanate the duplicate ones.
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums)
        ret = []
        previous = None
        for i in range(len(nums)):
            if previous == nums[i]:
                continue
            key = nums[i] * -1
            start = i + 1
            end = len(nums) - 1
            while(start < end):
                #print("%d %d %d" % (key, start, end))
                if nums[start] + nums[end] == key:
                    previous = nums[i]
                    one = []
                    one.append(nums[i])
                    one.append(nums[start])
                    one.append(nums[end])
                    ret.append(one)
                    
                    for k in range(start + 1, len(nums)):
                        if nums[k] != nums[start]:
                            start = k
                            break
                        start += 1
                    for k in range(end - 1, start + 1, -1):
                        if nums[k] != nums[end]:
                            end = k
                            break
                        end -= 1
                elif nums[start] + nums[end] > key:
                    end -= 1
                else:
                    start += 1
            #print(ret)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([0,0,0]))
    pass
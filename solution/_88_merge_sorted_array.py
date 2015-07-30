# -*- coding:utf-8 -*-
'''
Created on 2015/7/27

@author: dazhang

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Soluton:
Do not iterate from 0 to n, if do this, you must shift all elements many times
just iterate from m to 0, because nums1 is large enougth, or nums1's length is n + m - 1,
nums1 used for compare is only m, so we have enougth space to do.

'''

class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        retIndex = m + n - 1
        while(i >= 0 and j >= 0):
            if nums1[i] >= nums2[j]:
                nums1[retIndex] = nums1[i]
                i -= 1
            else:
                nums1[retIndex] = nums2[j]
                j -= 1
            retIndex -= 1
        # if nums2 left some ele, just append them to nums1
        while(j >= 0):
            nums1[retIndex] = nums2[j]
            j -= 1  
            retIndex -= 1     
        

if __name__ == '__main__':
    s = Solution()
    #nums1=[1,4,7,0,0,0,0,0]
    #s.merge(nums1,2,[2,3,6,8,9],5)
    nums1=[0]
    s.merge(nums1, 0, [1], 1)
    print(nums1)
    pass
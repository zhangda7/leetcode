#-*- coding:utf-8 -*-

'''
Created on 2015/7/23

@author: dazhang

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 <= k <= array's length.
'''

'''
Easier way, use num1 and num2 to save nums larger than key and smaller than key, than compare length of num1 and num2 to k.
Just quick sort, but no swap element, just copy to num1 and num2, easier.
Split nums to 3 section, 1.Larger than key, 2.Equal to key, 3.Smaller than key
if is in range 1, than recurution, k not change
if is in range 3, than recurution, change k
if not in 1 and 3, just return key
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if nums == None or len(nums) == 0:
            return 0
        #print(nums)
        key = nums[0]
        num1 = []
        num2 = []
        for i in range(1, len(nums)):
            if nums[i] > key:
                num1.append(nums[i])
            elif nums[i] < key:
                num2.append(nums[i])
                
        if len(num1) >= k:
            return self.findKthLargest(num1, k)
        elif (len(nums) - len(num2)) < k:
            return self.findKthLargest(num2, k - (len(nums) - len(num2)))
        return key

'''
harder one
use quick sort swap, use O(1) space
a little too diffcult
'''    
'''class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if nums == None or len(nums) == 0:
            return 0
        print(nums)
        left = 1
        right = len(nums) - 1
        key = nums[left]
        while left < right:
            while left < right:
                if nums[right] < key:
                    swap(nums, left, right)
                    left += 1
                    break
                right += 1
            while left < right:
                if nums[left] > key:
                    swap(nums, left, right)
                    right += 1
                    break
        if left >= k:
            self.findKthLargest(nums[:left], k)
        elif :
            self.findKthLargest(nums, k)'''
        
        
if __name__ == '__main__':
    s = Solution()
    #print(s.findKthLargest([3,2,1,5,6,4],6))
    print(s.findKthLargest([3,2,3,1,2,4,5,5,6], 9))
    pass
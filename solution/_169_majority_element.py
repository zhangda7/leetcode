'''
Created on 2015/7/22

@author: dazhang

Given an array of size n, find the majority element. The majority element is the element that appears more than  n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        dict = {}
        maxNum = 0
        maxKey = None
        for n in nums:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
            if maxNum < dict[n]:
                maxNum = dict[n]
                maxKey = n
        return maxKey
        
if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1,2,1,2,3,3,3]))
    pass
# -*- coding:utf-8 -*-
'''
Created on 2015/7/25

@author: dazhang

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Solution:
Keep an counter:


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
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[m]:
                if count >= 1:
                    continue
                else:
                    nums[m + 1] = nums[i]
                    m += 1
                    count += 1
            else:
                nums[m + 1] = nums[i]
                m += 1
                count = 0
        print(nums)
        return m + 1

class Solution2:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        m = 0 
        n = 0
        j = 0
        previousKey = ''
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[m]:
                if previousKey != nums[i]:
                    previousKey = nums[i]
                    count += 1
                    nums[m + 1] = nums[i]
                    m += 1
                else:
                    count += 1
                    if count >= 2:
                        continue
            else:
                nums[m + 1] = nums[i]
                m += 1
                previousKey = ''
                count = 0
        print(nums)
        return m + 1
        
        
        

if __name__ == '__main__':
    s = Solution()
    #print(s.removeDuplicates([0,1,1,2,2,2,2,3,3]))
    print(s.removeDuplicates([1,1,1,1,1,2,2,3,4,4,4,5,5,6]))
    pass
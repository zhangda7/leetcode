'''
Created on 2015/6/25

leetcode for 1-Two Sum
Use hashmap to implement O(n) execution time.

@author: dazhang
'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        kv = {}
        #init hashmap
        for i in range(len(nums)):
            kv[nums[i]] = i     
        for i in range(len(nums)):
            #calc left value
            left = target - nums[i]
            if left in kv and kv[left] != 0:
                return [i + 1, kv[left] + 1]
            
        pass

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([-1,-2,-3,-4,-5, -6, -9], -15))
    pass
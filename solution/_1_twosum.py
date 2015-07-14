'''
Created on 2015/6/25

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
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
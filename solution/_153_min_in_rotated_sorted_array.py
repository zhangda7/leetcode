'''
Created on 2015/7/16

@author: dazhang

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Solution:
very easy way:
such as below array:
4 5 6 7 8 9 0 1
0 1 2 3 4 5
4 5 0 1 2 3

when we find a range(i,j) to compare, make sure we compare n[i], n[j], n[mid]
not to compare n[mid -1], n[mid], n[mid + 1], this is the wrong way.
mid = (length / 2), 
Beacuse we need find the min, so we can find that : if n[j] < n[mid], then the min must in range(mid, j), because it is a roteted array
so we just need compare n[j] and n[mid], then detemine either range(mid, j) or range(i, mid)
'''

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        if nums == None or len(nums) == 0:
            return 0
        length = len(nums)
        i = 0
        j = length - 1
        while(True):
            mid = (i + j + 1) / 2
            #print("%d %d %d" % (i, j, mid))
            if nums[mid] > nums[j]:
                i = mid
            else:
                j = mid
            if (i + 1) >= j:
                return min(nums[i], nums[j])       

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([5, 6, 7, 0, 1]))
    #print(s.findMin([5,6,9,10,12,13,1,2]))
    pass
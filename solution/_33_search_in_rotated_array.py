'''
Created on 2015/7/17

@author: dazhang

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
http://blog.csdn.net/hackbuteer1/article/details/7581596
Solution:
This is not hard,just be clear that:
�����м�ֳ���������ʱ�����nums[mid] > nums[j],��(i, mid)�ǵ����ģ�����(mid, j)�ǵ����ģ�֮��ֻ���ж�target�Ƿ�����ε����������Ｔ��
������ڴ˶�����Ȼȥ��һ�����ң���ʵ�ܼ� 

'''

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return -1
        i = 0
        j = len(nums) - 1
        while(i <= j):
            mid = (i + j) / 2
            print("%d %d %d" % (i,j,mid))
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[j]:
                #means (mid, j) still is rotated array, (i, mid) is ascending array
                #still indicate min is in range(mid, j)
                if nums[i] <= target and nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                #means (mid, j is ascaending array)
                if nums[j] >= target and nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1
                    
        return -1
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.search([3,5,1], 3))
    
    
    pass
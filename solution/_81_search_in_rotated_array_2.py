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

'''

class Solution2:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return False
        i = 0
        j = len(nums) - 1
        while(i <= j):
            mid = (i + j) / 2
            #print("%d %d %d" % (i,j,mid))
            left = False
            if nums[mid] == target:
                return True
            if nums[mid] == nums[j] and mid < j:
                #This is the hardest part......
                #we need to detemine which range is asending
                #detemine which side is asending
                #search in (mid, j), if can find one smaller than mid + 1, then (mid, j) is not asending
                key = nums[j]
                for m in range(mid, j):
                    if nums[m] > key:
                        left = True
                        break
                if left == False:
                    #This means (mid, j) is all equal
                    key = nums[mid]
                    left = True
                    for n in range(i, mid):
                        if nums[n] > key:
                            left = False
                            break
                if left:
                    if nums[i] <= target and nums[mid] > target:
                        j = mid - 1
                    else:
                        i = mid + 1
                else:
                    if nums[j] >= target and nums[mid] < target:
                        i = mid + 1
                    else:
                        j = mid - 1
            elif nums[mid] > nums[j]:
                #means (mid, j) still is rotated array, (i, mid) is ascending array
                #just judge in range (i, mid)
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
                    
        return False
    
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if nums == None or len(nums) == 0:
            return False
        i = 0
        j = len(nums) - 1
        while(i <= j):
            mid = (i + j) / 2
            #print("%d %d %d" % (i,j,mid))
            left = False
            if nums[mid] == target:
                return True
            if nums[mid] == nums[j]:
                '''
                very easy way!
                just decrease j by 1 to escape the euqal one, Excellent!
                '''
                j -= 1
            elif nums[mid] > nums[j]:
                #means (mid, j) still is rotated array, (i, mid) is ascending array
                #just judge in range (i, mid)
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
                    
        return False
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.search([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 2))
    #print(s.search([3,1,1],3))
    
    pass
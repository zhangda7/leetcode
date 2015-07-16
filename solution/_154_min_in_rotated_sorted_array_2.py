'''
Created on 2015/7/16

@author: dazhang

Duplicate is allowed here

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
            elif nums[mid] == nums[j]:
                #need judge (mid, j) is decending or ascending
                #if we can find one less than nums[j] in (mid, j), then range is (mid, j), else is (i, mid) 
                end = nums[j]
                found = False
                for m in range(mid + 1, j):
                    #print(i)
                    if nums[m] < end:
                        i = mid
                        print("found")
                        found = True
                        break
                if not found:        
                    j = mid
            else:
                j = mid
            #print("%d %d %d" % (i, j, mid))
            if (i + 1) >= j:
                return min(nums[i], nums[j])       

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([0,4,4,4,4,4,4,4,4,4,4,4]))
    #print(s.findMin([5,6,9,10,12,13,1,2]))
    pass
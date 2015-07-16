'''
Created on 2015/7/16

@author: dazhang

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

ref:http://blog.csdn.net/a83610312/article/details/8548519

soultion: we can find the largest length, then we compare the height[i] and height[j], find the min, then find the next larger than min.

Because the length is shorter, we must find the larger length, so we can reach the max Container.

'''
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        if height == None or len(height) <= 1:
            return 0
        i = 0
        j = len(height) - 1
        ret = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            #print(area)
            if ret < area:
                ret = area
            if height[i] < height[j]:
                #increase i
                cur = height[i]
                while height[i] <= cur and i < j:
                    i += 1
            else:
                cur = height[j]
                while height[j] <= cur and i < j:
                    j -= 1
        return ret
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,2,4,3]))
    pass
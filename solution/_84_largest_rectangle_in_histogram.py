#-*- coding:utf-8 -*-
'''
Created on 2015/7/27

@author: dazhang

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.

Solution:

too dificult
http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
http://blog.csdn.net/abcbc/article/details/8943485

when h[k] >= h[k-1], select k is always better than k-1,
so if h[k] < h[k-1], just let right border is k-1, then select from left to compute area

'''

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        #Time limit exceed, but O(n) is a bit tricky, no means
        if height == None or len(height) == 0:
            return 0
        maxArea = 0
        for i in range(1, len(height)):
            if height[i] >= height[i-1]:
                continue
            for j in range(i - 1, -1, -1):
                area = min(height[j:i]) * (i - j)
                if area > maxArea:
                    maxArea = area
        return maxArea

if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2,1,5,6,2,3]))
    pass
# -*- coding:utf-8 -*-

'''
Created on 2015/8/19

@author: dazhang

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Do not think too diffuclut, 
From bottom to top

d[m][n] = min(d[m-1][n], d[m-1][n+1]) + triangle[m][n]
simple:
d[n] = min(d[n], d[n+1]) + triangle[m][n]

'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if triangle == None or len(triangle) == 0:
            return 0
        row = len(triangle)
        d = [0 for col in range(len(triangle[row-1]))]
        for i in range(len(triangle[row-1])):
            d[i] = triangle[row-1][i]
        for i in range(row-2, -1, -1):
            for j in range(len(triangle[i])):
                d[j] = min(d[j], d[j+1]) + triangle[i][j]
        return d[0]
        #for j in range(len())
            

if __name__ == '__main__':
    s = Solution()
    t = [[2], [3,4],[6,5,7],[4,1,8,3]]
    print(s.minimumTotal(t))
    pass
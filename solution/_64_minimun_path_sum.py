# -*- coding:utf-8 -*-

'''
Created on 2015/8/18

@author: dazhang

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

sum[i][j] = a[i][j] + min(a[i-1][j], a[i][j-1])
'''

class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if grid == None or len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        ret = [[0 for c in range(col)] for r in range(row)]
        ret[0][0] = grid[0][0]
        for i in range(1, row):
            ret[i][0] = ret[i-1][0] + grid[i][0]
        for j in range(1, col):
            ret[0][j] = ret[0][j-1] + grid[0][j]
        
        for i in range(1, row):
            for j in range(1, col):
                ret[i][j] = grid[i][j] + min(ret[i-1][j], ret[i][j-1])
        return ret[row-1][col-1]

if __name__ == '__main__':
    s = Solution()
    #grid = [[0 for col in range(2)] for row in range(2)]
    #grid[1][1] = 1
    grid = [[1,2], [1,1]]
    print(s.minPathSum(grid))
    pass
    pass
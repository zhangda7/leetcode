# -*- coding:utf-8 -*-

'''
Created on 2015/8/17

@author: dazhang
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
'''
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid == None:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m <= 0 or n <= 0:
            return 0
        ret = [[0 for col in range(n)] for row in range(m)]
        appear = False
        for i in range(m):
            if obstacleGrid[i][0] == 0 and not appear:
                ret[i][0] = 1
            else:
                ret[i][0] = -1
                appear = True
        appear = False
        for j in range(n):
            if obstacleGrid[0][j] == 0 and not appear:
                ret[0][j] = 1
            else:
                ret[0][j] = -1
                appear = True
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    ret[i][j] = -1
                else:
                    if ret[i-1][j] == -1:
                        ret[i][j] = ret[i][j-1]
                    elif ret[i][j-1] == -1:
                        ret[i][j] = ret[i-1][j]
                    else:
                        ret[i][j] = ret[i-1][j] + ret[i][j-1]
        return max(ret[m-1][n-1],0)
    
if __name__ == '__main__':
    s = Solution()
    grid = [[0 for col in range(3)] for row in range(3)]
    grid[1][1] = 1
    print(s.uniquePathsWithObstacles(grid))
    pass
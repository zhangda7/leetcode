# -*- coding:utf-8 -*-

'''
Created on 2015/8/17

@author: dazhang

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m <= 0 or n <= 0:
            return 0
        grid = [[0 for col in range(n)] for row in range(m)]
        ret = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            ret[i][0] = 1
        for j in range(n):
            ret[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                ret[i][j] = ret[i-1][j] + ret[i][j-1]
        return ret[m-1][n-1]
    
if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(3,4))
    pass
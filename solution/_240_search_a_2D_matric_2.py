# -*- coding:utf-8 -*-
'''
Created on 2015/7/30

@author: dazhang

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

Solution:
very burilient:
search from m[0][len(row) - 1], then if ele > target, then col--, else row ++

True, if m[i][j] < target, then all rows <= i will smaller than target, so i++
if m[i][j] > target, then all cols >= j will larger than target, so j--

'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while(row < len(matrix) and col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False



if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20], [23,30,34,50]], 23))
    #print(s.searchMatrix([[1],[3]],3))
    pass
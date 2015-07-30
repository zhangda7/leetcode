# -*- coding:utf-8 -*-
'''
Created on 2015/7/30

@author: dazhang

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return False
        rowIndex = 0
        for i in range(0, len(matrix)):
            row = matrix[i]
            if len(row) == 0:
                continue
            if row[0] <= target and row[len(row) - 1] >= target:
                rowIndex = i
                break
        for num in matrix[rowIndex]:
            if num == target:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20], [23,30,34,50]], 23))
    #print(s.searchMatrix([[1],[3]],3))
    pass
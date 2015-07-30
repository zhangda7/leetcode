# -*- coding:utf-8 -*-
'''
Created on 2015/7/26

@author: dazhang

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

Solution:
a[i][j] = a[i-1][j-1] + a[i-1][j] j < length / 2
        j = length - j, j > length / 2
        
just find the bilateral index, it is easy
The begin and last always is 1, can force it to simeplify error path.

-------------
Update:
-------------
Forget about split it to 2, if we force the first and the last to 1, we will not encounter array out of index, so just use one euqation:
a[i][j] = a[i-1][j-1] + a[i-1][j]
'''

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        ret = []
        if numRows <= 0:
            return ret
        col = 2
        ret.append([1])
        for i in range(1, numRows):
            row = []
            row.append(1)
            for j in range(1, col - 1):
                #if j <= col / 2:
                row.append(ret[i-1][j-1] + ret[i-1][j])
                #else:
                #    index = col - j - 1
                #    row.append(ret[i-1][index-1] + ret[i-1][index])
            row.append(1)        
            col += 1
            ret.append(row)
            #print(ret)
        return ret

if __name__ == '__main__':
    s = Solution()
    print(s.generate(6))
    pass
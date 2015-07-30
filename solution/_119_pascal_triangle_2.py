# -*- coding:utf-8 -*-
'''
Created on 2015/7/27

@author: dazhang

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?


Solution():
a[i][j] = a[i-1][j-1] + a[i-1][j]

use O(2k) is OK. This is not the best way.

See the euqation, can see that a[i][j] only matters j-1 and j, so we for j in range(col, 0, -1)
we can only use one O(k) array to implement this.

'''

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        if rowIndex < 0:
            return []
        ret = []
        rowIndex += 1
        for i in range(rowIndex):
            ret.append(1)
        for i in range(1, rowIndex):
            for j in range(i - 1, 0, -1):
                ret[j] = ret[j] + ret[j - 1]
            #print(ret)    
        return ret
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(3))
    pass
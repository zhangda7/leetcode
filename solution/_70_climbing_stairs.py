# -*- coding:utf-8 -*-
'''
Created on 2015/7/23

@author: dazhang

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        '''if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n - 2)'''
        if n == 1:
            return 1
        if n == 2:
            return 2
        '''ret = []
        for i in range(n):
            ret.append(0)
        ret[0] = 1
        ret[1] = 2
        for i in range(2, n):
            ret[i] = ret[i - 1] + ret[i - 2]
        return ret[n - 1]'''
        x = 0
        y = 1
        z = 2
        for i in range(2,n):
            x = y + z
            y = z
            z = x
        return x
        

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(35))
    pass
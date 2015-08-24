# -*- coding:utf-8 -*-

'''
Created on 2015年8月17日

@author: dazhang

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Solution:
convert to find MAX(a[j] - a[i]), j > i, if not found, return 0

'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if prices == None or len(prices) == 0:
            return 0
        ret = []
        for i in range(len(prices)):
            ret.append(0)
        minV = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= prices[i - 1]:
                ret[i] = ret[i - 1]
            else:
                ret[i] = prices[i] - minV
            if prices[i] < minV:
                minV = prices[i]
        print ret
        return max(ret)

if __name__ == '__main__':
    p = [2,4,7,1,2,9]
    s = Solution()
    print(s.maxProfit(p))
    pass
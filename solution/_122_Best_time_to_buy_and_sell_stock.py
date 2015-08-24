# -*- coding:utf-8 -*-

'''
Created on 2015/8/17

@author: dazhang

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Solution:
不要想的太复杂了，这题的意思是，一天内既可买入也可卖出，所以比较简单了：
我们在第i天买入，如果发现i + 1天比i高，那么就可以累加到利润里面。
'''

class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if prices == None or len(prices) < 2:
            return 0
        sum = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                sum += prices[i] - prices[i-1]
        return sum
        

if __name__ == '__main__':
    p = [2,4,7,1,2,9]
    s = Solution()
    print(s.maxProfit(p))
    pass
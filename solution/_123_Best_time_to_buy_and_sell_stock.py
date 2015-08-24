# -*- coding:utf-8 -*-

'''
Created on 2015/8/17

@author: dazhang

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

可以进行最多两次买入和卖出，所以这时可以考虑“分治”的方法，分界线从0-n, 这样就即包含最多一次的情况，也包含了两次的情况，再求最大值就可以了。
'''
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    '''
    具体方法是这样，先记录p[1:i]的maxProfit, 记录到一个数组里，之后再计算p[i:n]的maxProfit, 逆序计算就可以，之后再计算最大值就可以了，这样只需要O(n)
    '''
    def maxProfit(self, prices):
        if prices == None or len(prices) == 0:
            return 0
        n = len(prices)
        profit_front = [0] * n
        profit_back = [0] * n
        minV = prices[0]
        for i in range(1, n):
            profit_front[i] = max(profit_front[i-1], prices[i] - minV)
            minV = min(minV, prices[i])
        maxV = prices[n-1]
        for i in range(n - 2, -1, -1):
            profit_back[i] = max(profit_back[i+1], maxV - prices[i])
            maxV = max(maxV, prices[i])
        maxRet = 0
        for i in range(n):
            maxRet = max(maxRet, profit_front[i] + profit_back[i])
        return maxRet
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit2(self, prices):
        #Time limit Exceed, cause it need O(n**2)
        if prices == None or len(prices) == 0:
            return 0
        sum = 0
        maxSum = 0
        for i in range(len(prices)):
            sum = self.maxProfit1(prices[:i]) + self.maxProfit1(prices[i:])
            maxSum = max(sum, maxSum)
        return maxSum    
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit1(self, prices):
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
        return max(ret)

if __name__ == '__main__':
    p = [2,4,7,1,2,9]
    s = Solution()
    print(p[:1])
    print(p[1:])
    print(s.maxProfit(p))
    pass
    pass
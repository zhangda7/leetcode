'''
Created on 2015/7/14

@author: dazhang

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Attention:
1.x = 0
2.x < 0, such as -123
3.x is larger than Int.Max, but this will not occor in python, so assume this is 32-bit integer, range is (-2147483647, 2147483647)
'''
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        digits = []
        positive = 1
        if x == 0:
            return 0
        if x < 0:
            positive = -1
            x = x * -1
        while (x > 0):
            digits.append(x % 10)
            x = x / 10
        ret = 0
        for i in range(len(digits)):
            ret = int(digits[i]) + ret * 10
        if abs(ret) > 2147483647:
            ret = 0 
        return ret * positive   
if __name__ == '__main__':
    s = Solution()
    print(s.reverse(2147483647))
    pass
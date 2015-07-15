'''
Created on 2015/7/15

@author: dazhang

String to Integer (atoi) Total Accepted: 55271 Total Submissions: 426876 My Submissions Question Solution 
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

UT:
1 -> 1
-123 -> -123
-12acd12 -> -12
   120 -> 120
     +0 123 -> 0
-2147483648 -> -2147483648
123  456 -> 123
'''

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        if str == None or len(str) == 0:
            return 0
        ret = 0
        positive = 1
        postiveSet = False
        numBegin = False
        for c in str:
            if c == ' ':
                if numBegin:
                    break
                continue
            else:
                numBegin = True
            if not ((c >= '0' and c <= '9') or c == '-' or c == '+'):
                break
            if c == '-':
                if postiveSet:
                    return 0
                positive = -1
                postiveSet = True
                continue
            elif c == '+':
                if postiveSet:
                    return 0
                positive = 1
                postiveSet = True
                continue
            else:
                ret = ret * 10 + int(c)
        ret = ret * positive
        if ret > 2147483647:
            return 2147483647
        if ret < -2147483647:
            return -2147483648
        return ret
        
        

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("  +0 123"))
    pass
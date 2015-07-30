'''
Created on 2015/7/15

@author: dazhang

Palindrome Number Total Accepted: 66615 Total Submissions: 234550 My Submissions Question Solution 
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

Solution:
no extra space, so we can not put it in a list, so there is 2 way to solve:
1.reverse Integer without string, then compare the result and the original, we can reverse a integer without a list, but this will exceed
2.Directly get the fist number and the last number, then the second and the second last...
such as 83401:
    first 8 = 83401 / 10**4
    last 1 = 83401 % 10

Attention:

-123321 -> False, i.e negtive number always is False

Upper is too complicated, just reverse the number, then compare it with the original one.
Attention: In python, this is OK, but in c, reverse the number may exceed INT_MAX, so this may not be the best way

'''
class Solution2:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0 :
            return False
        num = x
        length = 0
        while (num != 0):
            length += 1
            num = num / 10
        num = x
        for i in range(length / 2):
            first = (num / (10**(length - i - 1))) % 10
            last = (num / 10 ** (i)) % 10
            #print("%d %d" % (first, last))
            if first != last:
                return False
        return True
    
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x < 0 :
            return False
        num = x
        length = 0
        rev = 0
        while (num != 0):
            rev = num % 10 + rev * 10
            num /= 10
        if rev == x:
            return True
        else:
            return False
        
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(112221211))
    pass
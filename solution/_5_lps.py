'''
Created on 2015/7/1

@author: dazhang
'''
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        start = 0
        end = 0
        maxLength = 0
        equalLength = 0
        for i in range(1, len(s)):
            #print("---i %d---" % (i))
            for j in range(0,i):
                if (i + j) >= len(s):
                    break
                #print("%s %s" % (s[i + j], s[i - j - 1]))
                if s[i + j] != s[i - j - 1]:
                    break
                else:
                    equalLength += 1
            if maxLength < 2 * equalLength:
                maxLength = 2 * equalLength
            equalLength = 0
            #print(maxLength)
            for j in range(1,i+1):
                if (i + j) >= len(s):
                    break
                #print("%s %s" % (s[i + j], s[i - j]))
                if s[i + j] != s[i - j]:
                    break
                else:
                    equalLength += 1
            #print(equalLength)
            if maxLength < (2 * equalLength) + 1:
                maxLength = (2 * equalLength) + 1
            equalLength = 0
            #print(maxLength)
        if len(s) <= 1:
            maxLength = len(s)
        return maxLength
if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abbbba"))
    pass

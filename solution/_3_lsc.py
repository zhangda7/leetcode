'''
Created on 2015/6/26

@author: dazhang
'''

'''
Solution of O(N^2)
'''
class Solution_N2:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        cDict = {}
        maxLength = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in cDict:
                    if len(cDict) > maxLength:
                        maxLength = len(cDict)
                    cDict = {}
                    break
                else:
                    cDict[s[j]] = 1
                    #print(len(cDict))
        return maxLength

'''
Solution of O(N)
'''
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):
        cDict = {}
        maxLength = 0
        curLength = 0
        lastStart = 0
        for i in range(len(s)):
            cDict[s[i]] = -1
        for i in range(len(s)):
            if cDict[s[i]] == -1:
                curLength += 1
                cDict[s[i]] = i
            else:
                print("%d : %d %s %d %d" % (i, lastStart, s[i], cDict[s[i]], curLength))
                if lastStart <= cDict[s[i]]:
                    curLength = i - cDict[s[i]]
                    lastStart = cDict[s[i]] + 1
                    cDict[s[i]] = i
                else:
                    curLength += 1
                    cDict[s[i]] = i
                    
            if maxLength < curLength:
                maxLength = curLength
        if len(s) <=1:
            maxLength = len(s)
        return maxLength       
                

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("aua"))
    print(s.lengthOfLongestSubstring("qwnfenpglqdq"))
    pass
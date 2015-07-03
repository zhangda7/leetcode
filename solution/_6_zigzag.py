# -*- coding: cp936 -*-
'''
use tuple should be faster
'''
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if len(s) == 0 or numRows == 0:
            return ""
        oneColumn = True
        curColumn = 0
        isAdd = 1
        curRow = 0
        #ret = [i for i in range(numRows), 1,[]]
        ret = []
        for i in range(numRows):
            row = []
            for j in range(len(s)/numRows + 1):
                row.append(' ')
            ret.append(row)
        for i in range(len(s)):
            if len(ret[curRow]) <= curColumn:
                length = len(ret[curRow])
                for j in range(length, curColumn + 1):
                    ret[curRow].append(' ')
            ret[curRow][curColumn] = s[i]
            curRow, isAdd, oneColumn = self.getNextRow(curRow, numRows, isAdd, oneColumn)
            if not oneColumn:
                curColumn += 1
        for l in ret:
            print(l)
        result = []        
        for l in ret:
            #print("".join(l))
            result.append("".join(l))
        #print("".join(result).replace(" ",""))
        return "".join(result).replace(" ","")
            
    def getNextRow(slef, curRow, numRows, isAdd, oneColumn):
        curRow = curRow + 1 * isAdd
        if numRows == 1:
            return (0, isAdd, False)
        if curRow == numRows:
            curRow -= 2
            isAdd = -1
            oneColumn = not oneColumn
        elif curRow == -1:
            curRow = 1
            isAdd = 1
            oneColumn = not oneColumn
        return (curRow, isAdd, oneColumn)
            

if __name__ == "__main__":
    s = Solution()
    print(s.convert("ABCDE", 3))

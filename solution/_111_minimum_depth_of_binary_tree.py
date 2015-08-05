# -*- coding:utf-8 -*-

'''
Created on 2015/8/5

@author: dazhang

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2:
    # @param {TreeNode} root
    # @return {integer}
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        l = 2**32
        r = 2**32
        if root.left != None:
            l = self.minDepth(root.left) + 1
        if root.right != None:
            r = self.minDepth(root.right) + 1
        #print l,r
        return min(l,r)
    
class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        nodes = []
        # a length array, indicate to the nodes's length
        # because for backtrace, we need the previous length
        # when go to a leaf node, we need back trace, then use the previous length
        l = []
        length = 0
        minLength = 2**32
        nodes.append(root)
        l.append(0)
        while(len(nodes) > 0):
            length += 1
            cur = nodes.pop()
            curL = l.pop()
            if cur.right == None and cur.left == None:
                minLength = min(length, minLength)
                if len(l) > 0:
                    # if len == 0, means the last node, so no need to set length again
                    length = l[len(l) - 1]
            if cur.right != None:
                nodes.append(cur.right)
                l.append(length)
            if cur.left != None:
                nodes.append(cur.left)
                l.append(length)
        return minLength    
            
if __name__ == '__main__':
    root = TreeNode(1)
    l1 = TreeNode(2)
    l2 = TreeNode(3)
    l3 = TreeNode(4)
    l4 = TreeNode(5)
    l5 = TreeNode(5)
    l6 = TreeNode(5)
    #root.left = l1
    root.right = l2
    l6.left = l3
    l2.left = l4
    l4.left = l5
    l5.left = l6
    s = Solution()
    print(s.minDepth(root))
    pass
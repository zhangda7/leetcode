# -*- coding:utf-8 -*-

'''
Created on 2015/8/24

@author: dazhang

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        height = self.getHeight(root)
        if height < 0:
            return False
        return True
    def getHeight(self, root):
        if root == None:
            return 0
        leftHeight = self.getHeight(root.left) + 1
        rightHeight = self.getHeight(root.right) + 1
        #print leftHeight, rightHeight
        if abs(leftHeight - rightHeight) > 1:
            #找到一个不符合的，就已经不符合了，设一个很小的数，最后判断就好了
            return -2**32
        else:
            return max(leftHeight, rightHeight)

if __name__ == '__main__':
    root = TreeNode(0)
    l1 = TreeNode(1)
    l2 = TreeNode(1)
    l3 = TreeNode(2)
    l4 = TreeNode(2)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    root.left = l1
    root.right = l2
    l1.right = l3
    l2.right = l4
    l4.right = l5
    l5.left = l6
    s = Solution()
    print(s.isBalanced(root))
    pass
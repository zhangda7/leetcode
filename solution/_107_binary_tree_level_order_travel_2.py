# -*- coding:utf-8 -*-

'''
Created on 2015/8/24

@author: dazhang

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

Solution:Easy, just for each each level, double while iteration.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret = []
        nodes = []
        nodes.append(root)
        ret.append([root.val])
        while(len(nodes) > 0):
            newNodes = []
            retVal = []
            while(len(nodes) > 0):
                node = nodes.pop(0)
                if node.left != None:
                    newNodes.append(node.left)
                    retVal.append(node.left.val)
                if node.right != None:
                    newNodes.append(node.right)
                    retVal.append(node.right.val)
                    
            #print ret, newNodes
            if len(retVal) > 0:
                ret.insert(0, retVal)
            nodes = newNodes
        return ret

if __name__ == '__main__':
    root = TreeNode(0)
    l1 = TreeNode(1)
    l2 = TreeNode(2)
    l3 = TreeNode(3)
    l4 = TreeNode(4)
    l5 = TreeNode(5)
    l6 = TreeNode(6)
    root.left = l1
    root.right = l2
    l1.left = l3
    l2.left = l4
    l2.right = l5
    l5.left = l6
    s = Solution()
    print(s.levelOrderBottom(root))
    pass
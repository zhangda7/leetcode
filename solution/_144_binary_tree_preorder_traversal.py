# -*- coding:utf-8 -*-

'''
Created on 2015/8/20

@author: dazhang

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

preorder : root, left, right, root must print, if left and right has child, visit child first.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return []
        ret.append(root.val)
        ret.extend(self.preorderTraversal(root.left))
        ret.extend(self.preorderTraversal(root.right))
        
        return ret
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return []
        stack = []
        stack.append(root)
        while(len(stack) > 0):
            cur = stack.pop()
            ret.append(cur.val)
            if cur.right != None:
                stack.append(cur.right)
            if cur.left != None:
                stack.append(cur.left)
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
    print(s.preorderTraversal(root))
    pass
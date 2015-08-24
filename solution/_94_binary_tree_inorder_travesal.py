# -*- coding:utf-8 -*-

'''
Created on 2015/8/20

@author: dazhang
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
首先需要一直对左子树迭代并将非空节点入栈
节点指针为空后不再入栈
当前节点为空时进行出栈操作，并访问栈顶节点
将当前指针p用其右子节点替代
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return []
        ret.extend(self.inorderTraversal(root.left))
        ret.append(root.val)
        ret.extend(self.inorderTraversal(root.right))        
        return ret
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodes = []
        result = []
        if root == None:
            return None
        while(len(nodes) > 0 or root != None):
            if root != None:
                nodes.append(root)
                root = root.left
            else:
                root = nodes.pop()
                result.append(root.val)
                root = root.right
        return result
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
    print(s.inorderTraversal(root))
    pass
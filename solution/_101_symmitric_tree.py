# -*- coding:utf-8 -*-

'''
Created on 2015/8/24

@author: dazhang

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return True
        nodes = []
        nodes.append(root)
        while(len(nodes) > 0):
            newNodes = []
            retVal = []
            while(len(nodes) > 0):
                node = nodes.pop(0)
                if node == None:
                    continue
                if node.left != None:
                    newNodes.append(node.left)
                    retVal.append(node.left.val)
                else:
                    newNodes.append(None)
                    retVal.append(None)
                if node.right != None:
                    newNodes.append(node.right)
                    retVal.append(node.right.val)
                else:
                    newNodes.append(None)
                    retVal.append(None)
                    
            #detemine retVal whether is symmtric
            mid = len(retVal) / 2
            print retVal
            for i in range(mid):
                if retVal[i] != retVal[-1 - i]:
                    return False
            
            nodes = newNodes
        return True

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
    #l2.right = None
    #l5.left = l6
    s = Solution()
    print(s.isSymmetric(root))
    pass
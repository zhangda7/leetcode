# -*- coding:utf-8 -*-

'''
Created on 2015/8/20

@author: dazhang
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

规则是左右根，其中左和右都要递归


蛮麻烦的，两个变量：1.nochild，按我们的规则，如果一个节点nochild，则肯定要输出的节点；2、visitied，记录两个指针，prev和cur，如果prev是cur的孩子，那么说明此时要输出cur了，比如下面先输出3，再输出2的时候就要判断
visited了，要不又要再遍历3，就不对了。
      1
     /
    2
   /
  3 
'''
import time
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution2(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if root == None:
            return []
        ret.extend(self.postorderTraversal(root.left))
        ret.extend(self.postorderTraversal(root.right))   
        ret.append(root.val)     
        return ret
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        result = []
        nodes = []
        nodes.append(root)
        prev = None
        while(len(nodes) > 0):
            root = nodes[-1]
            #print root.val, result
            #printTree(nodes)
            #time.sleep(1)
            nochild = (root.left == None and root.right == None)
            visited = (prev != None and (root.left == prev or root.right == prev))
            if nochild or visited:
                result.append(root.val)
                prev = root
                nodes.pop()
            else:
                if root.right != None:
                    nodes.append(root.right)
                if root.left != None:
                    nodes.append(root.left)
        return result
def printTree(tree):
    for t in tree:
        print t.val,
    print ""
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
    print(s.postorderTraversal(root))
    s = [1,2,3]
    print(s[-1])
    pass
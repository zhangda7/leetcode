#-*- coding:utf-8 -*-

'''
Created on 2015/8/24

@author: dazhang

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

#easy but ugly solution
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        if p == None or q == None:
            return False
        if p.val != q.val:
            return False
        pnodes = []
        pnodes.append(p)
        qnodes = []
        qnodes.append(q)
        while(len(pnodes) > 0 and len(qnodes) > 0):
            pnewNodes = []
            pretVal = []
            while(len(pnodes) > 0):
                node = pnodes.pop(0)
                if node == None:
                    continue
                if node.left != None:
                    pnewNodes.append(node.left)
                    pretVal.append(node.left.val)
                else:
                    pnewNodes.append(None)
                    pretVal.append(None)
                if node.right != None:
                    pnewNodes.append(node.right)
                    pretVal.append(node.right.val)
                else:
                    pnewNodes.append(None)
                    pretVal.append(None)
                    
            qnewNodes = []
            qretVal = []
            while(len(qnodes) > 0):
                node = qnodes.pop(0)
                if node == None:
                    continue
                if node.left != None:
                    qnewNodes.append(node.left)
                    qretVal.append(node.left.val)
                else:
                    qnewNodes.append(None)
                    qretVal.append(None)
                if node.right != None:
                    qnewNodes.append(node.right)
                    qretVal.append(node.right.val)
                else:
                    qnewNodes.append(None)
                    qretVal.append(None)
            #print pretVal, qretVal
            if len(pretVal) != len(qretVal):
                return False
            for i in range(len(pretVal)):
                if pretVal[i] != qretVal[i]:
                    return False
            pnodes = pnewNodes
            qnodes = qnewNodes
            if len(pnodes) != len(qnodes):
                return False
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
    print(s.isSameTree(root, l1))
    pass
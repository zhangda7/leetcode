# -*- coding:utf-8 -*-

'''
Created on 2015��8��24��

@author: dazhang

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
               1
        --------|-------
        2               3
    ----|----       ----|----
    4       5       6       7
具体到上面这一题，我们知道了一个二叉树的中序遍历以及后序遍历的结果，那么如何构建这颗二叉树呢？

仍然以上面那棵二叉树为例，我们可以发现，对于后序遍历来说，最后一个元素一定是根节点，也就是1。然后我们在中序遍历的结果里面找到1所在的位置，那么它的左半部分就是其左子树，有半部分就是其右子树。

我们将中序遍历左半部分425取出，同时发现有序遍历的结果也在相应的位置上面，只是顺序稍微不一样，也就是452。我们可以发现，后序遍历中的2就是该子树的根节点。

上面说到了左子树，对于右子树，我们取出637，同时发现后序遍历中对应的数据偏移了一格，并且顺序也不一样，为673。而3就是这颗右子树的根节点。

重复上述过程，通过后续遍历找到根节点，然后在中序遍历数据中根据根节点拆分成两个部分，同时将对应的后序遍历的数据也拆分成两个部分，重复递归，就可以得到整个二叉树了。
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == None or postorder == None or len(inorder) == 0 or len(postorder) == 0:
            return None
        
        if (True):
            root = TreeNode(postorder[-1])
            curVal = root.val
            curRoot = root
            leftDict = {}
            rightDict = {}
            toLeft = True
            index = -1
            for i in range(len(inorder)):
                if inorder[i] == curVal:
                    toLeft = False
                    index = i
                    continue
                if toLeft:
                    leftDict[inorder[i]] = True
                else:
                    rightDict[inorder[i]] = True
            #print leftDict, "--", rightDict
            leftIndex = 0
            for i in range(len(postorder) - 1, -1, -1):
                if postorder[i] in leftDict:
                    #print "left:", inorder[:index], postorder[:i + 1]
                    leftDict = None
                    curRoot.left = self.buildTree(inorder[:index], postorder[:i + 1])
                    break
            for i in range(len(postorder)):
                if postorder[i] in rightDict:
                    #print "right:", inorder[index + 1:], postorder[i:-1]
                    rightDict = None
                    curRoot.right = self.buildTree(inorder[index + 1:], postorder[i:-1])
                    break
            return root
        
if __name__ == '__main__':
    s = Solution()
    #ret = s.buildTree([4,2,1,3],[4,2,3,1])
    ret = s.buildTree([4,2,5,1,6,3,7],[4,5,2,6,7,3,1])
    print(s.preorderTraversal(ret))
    pass
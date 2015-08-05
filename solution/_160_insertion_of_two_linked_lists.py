# -*- coding:utf-8 -*-

'''
Created on 2015/8/5

@author: dazhang

Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

这题需要得到两个链表的交接点，也就是c1，这一题也很简单。

遍历A，到结尾之后，将A最后的节点连接到B的开头，也就是c3 -> b1
使用两个指针fast和slow，从a1开始，判断是否有环
如果没环，在返回之前记得将c3 -> b1给断开
如果有环，则按照第二题的解法得到c1，然后断开c3 -> b1
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        p1 = head
        p2 = head
        while(p1!= None and p2!= None):
            #print p1.val, p2.val
            p1 = p1.next
            if p2.next != None:
                p2 = p2.next.next
            else:
                return None
            if p1 == p2:
                break
        p2 = head
        while(p1!= None and p2!= None):
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
        p1 = headA
        while(p1.next != None):
            p1 = p1.next
        #now p1 is the last node of headA
        p2 = headB
        p1.next = p2
        ret = self.detectCycle(headA)
        p1.next = None
        return ret
        

if __name__ == '__main__':
    pass
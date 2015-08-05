# -*- coding:utf-8 -*-

'''
Created on 2015/8/5

@author: dazhang

Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Follow up:
Can you solve it without using extra space?
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
        
        

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s4 = ListNode(4)
    s5 = ListNode(5)
    s6 = ListNode(6)
    s1.next = None
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = s6
    s = Solution()
    print(s.detectCycle(s1))
    pass
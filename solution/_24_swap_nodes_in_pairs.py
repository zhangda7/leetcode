# -*- coding:utf-8 -*-

'''
Created on 2015/8/10

@author: dazhang

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def swapPairs(self, head):
        if head == None:
            return None
        pre = head
        cur = head
        count = 0
        #each time we swap cur and cur.next
        while(cur != None):
            if cur.next == None:
                break
            if pre == head:
                head = cur.next
            tmp = cur.next.next
            cur.next.next = cur
            pre.next = cur.next
            cur.next = tmp
            pre = cur
            cur = tmp
        return head
        

def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val)
        head = head.next

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s4 = ListNode(4)
    s5 = ListNode(5)
    s6 = ListNode(6)
    s1.next = s2
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = None
    s = Solution()
    printList(s.swapPairs(s1))
    pass
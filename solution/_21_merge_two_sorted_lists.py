# -*- coding:utf-8 -*-

'''
Created on 2015/8/7

@author: dazhang

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = None
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
        cur = head
        while(l1 != None and l2 != None):
            if l1.val <= l2.val:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2
        return head
    
def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val)
        head = head.next

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(6)
    s3 = ListNode(8)
    s4 = ListNode(3)
    s5 = ListNode(4)
    s6 = ListNode(5)
    s1.next = s2
    s2.next = s3
    s3.next = None
    s4.next = s5
    s5.next = s6
    s6.next = None
    s = Solution()
    printList(s.mergeTwoLists(s1,s4))
    pass
# -*- coding:utf-8 -*-

'''
Created on 2015/8/7

@author: dazhang

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Solution:
divide and conqer, first two two merge, then two two result merge...
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.mergeTwoLists(self.mergeKLists(lists[:len(lists) / 2]), self.mergeKLists(lists[len(lists)/2:]))
        
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
    s4.next = None
    s5.next = s6
    s6.next = None
    ll = [s1,s4,s5]
    s = Solution()
    printList(s.mergeKLists(ll))
    pass
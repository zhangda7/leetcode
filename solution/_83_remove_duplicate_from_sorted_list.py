# -*- coding:utf-8 -*-

'''
Created on 2015/8/7

@author: dazhang

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None:
            return None
        cur = head
        pre = head
        val = cur.val
        while(cur != None):
            cur = cur.next
            if cur == None:
                break
            if cur.val != val:
                val = cur.val
                pre = cur
                continue
            else:
                pre.next = cur.next
                cur = pre
                #delete cur
        return head
        
def printList(head):
    while(head != None):
        print(head.val)
        head = head.next

if __name__ == '__main__':
    s1 = ListNode(2)
    s2 = ListNode(2)
    s3 = ListNode(2)
    s4 = ListNode(2)
    s5 = ListNode(2)
    s6 = ListNode(2)
    s1.next = s2
    s2.next = s3
    s3.next = None
    s4.next = s5
    s5.next = s6
    s6.next = None
    #printList(s1)
    s = Solution()
    printList(s.deleteDuplicates(s1))
    pass
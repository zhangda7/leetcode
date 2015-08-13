# -*- coding:utf-8 -*-

'''
Created on 2015/8/12

@author: dazhang

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if head == None:
            return None
        p1 = head
        p2 = head.next
        p1.next = None
        p3 = head
        while(p2 != None):
            p3 = p2.next
            p2.next = p1
            head = p2
            p1 = p2
            p2 = p3
        return head
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        if head == None:
            return None
        if head.next == None:
            return
        length = 0
        cur = head
        while(cur != None):
            length += 1
            cur = cur.next
        cur = head
        middle = head
        length = length / 2
        count = 0
        while(cur != None):
            count += 1
            if count > length + 1:
                middle = middle.next
            cur = cur.next
        #print middle.val
        tmp = middle.next
        middle.next = None
        middle = self.reverseList(tmp)
        #printList(head)
        #printList(middle)
        cur = head
        normal = True
        while(cur != None and middle != None):
            #printList(head)
            if normal:
                tmp = cur.next
                cur.next = middle
                cur = tmp
                normal = False
            else:
                tmp = middle.next
                middle.next = cur
                middle = tmp
                normal = True
        return
        

def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val),
        head = head.next
    print ""

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
    s4.next = None
    s5.next = None
    s6.next = None
    s = Solution()
    printList(s.reorderList(s1))
    pass
# -*- coding:utf-8 -*-

'''
Created on 2015年8月13日

@author: dazhang

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} x
    # @return {ListNode}
    def partition(self, head, x):
        if head == None:
            return None
        dummy = ListNode(x + 1)
        dummy.next = head
        cur = dummy
        rep = dummy
        while(cur.next != None):
            printList(dummy.next)
            if cur.next.val < x:
                #in this, means we may have to change
                print cur.val, cur.next.val, rep.val,rep.next.val
                if cur != rep:
                    tmp = cur.next.next
                    cur.next.next = rep.next
                    rep.next = cur.next
                    cur.next = tmp
                    rep = rep.next
                else:
                    # cur == rep, means cur and rep is the head element, no need to move
                    cur = cur.next
                    rep = rep.next
            else:
                cur = cur.next
        return dummy.next         

def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val),
        head = head.next
    print ""

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(7)
    s3 = ListNode(0)
    s4 = ListNode(3)
    s5 = ListNode(1)
    s6 = ListNode(2)
    s7 = ListNode(1)
    s8 = ListNode(0)
    s9 = ListNode(2)
    s10 = ListNode(3)
    s11 = ListNode(4)
    s12 = ListNode(1)
    s13 = ListNode(0)
    s14= ListNode(2)
    s1.next = s2
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = s7
    s7.next = s8
    s8.next = s9
    s9.next = s10
    s10.next = s11
    s11.next = s12
    s12.next = s13
    s13.next = s14
    s14.next = None
    s = Solution()
    printList(s.partition(s1, 2))
    pass
# -*- coding:utf-8 -*-

'''
Created on 2015/8/7

@author: dazhang

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

Must use 3 pointers, prepre, pre, cur, when same, prepre->next = cur, this is true.
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
        prepre = head
        val = cur.val
        while(cur != None):
            #print("%d %d %d" % (prepre.val, pre.val, cur.val))
            cur = cur.next
            if cur == None:
                break
            if cur.val != val:
                prepre = pre
                pre = cur
                val = cur.val
                continue
            else:
                while(cur != None and cur.val == val):
                    cur = cur.next
                if pre == head:
                    prepre = cur
                    head = cur
                    pre = cur
                else:
                    prepre.next = cur
                    pre = cur
                if cur == None:
                    break
                val = cur.val
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
    s3 = ListNode(2)
    s4 = ListNode(3)
    s5 = ListNode(3)
    s6 = ListNode(4)
    s1.next = s2
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = None
    #printList(s1)
    s = Solution()
    printList(s.deleteDuplicates(s1))
    pass
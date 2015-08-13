# -*- coding:utf-8 -*-

'''
Created on 2015/8/7

@author: dazhang

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        #a little diffcult
        pass
    
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
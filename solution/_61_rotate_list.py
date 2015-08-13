# -*- coding:utf-8 -*-

'''
Created on 2015/8/12

@author: dazhang
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.


Because we need handle k > length(list), so we must know list length first.
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
    def rotateRight(self, head, k):
        if head == None:
            return None
        
        count = 0
        cur = head
        last = head
        length = 0
        while(last != None):
            length += 1
            last = last.next
        k = k % length
        last = head
        #print k
        if k == 0:
            return head
        while(last.next != None):
            count += 1
            if count > k:
                cur = cur.next
            last = last.next
        #print count + 1
        #now cur.next is new head
        #last is the last None node
        
        tmp = cur.next
        cur.next = None
        last.next = head
        head = tmp
        
        return head
        
        

def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val),
        head = head.next

if __name__ == '__main__':
    s1 = ListNode(1)
    s2 = ListNode(2)
    s3 = ListNode(3)
    s4 = ListNode(4)
    s5 = ListNode(5)
    s6 = ListNode(6)
    s1.next = s2
    s2.next = None
    s3.next = s4
    s4.next = s5
    s5.next = None
    s6.next = None
    s = Solution()
    printList(s.rotateRight(s1,4))
    pass
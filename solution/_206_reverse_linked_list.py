'''
Created on 2015/7/16

@author: dazhang

Reverse a singly linked list.

remember 3 pointer, p1 , p2, p3

         1 -> 2 -> 3 -> 4 -> 5
round 1: p1   p2   p3
round 2:      p1   p2   p3
round 3:           p1   p2   p3
Terminal : p2 == None

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if head == None:
            return
        p1 = head
        p2 = p1.next
        p1.next = None
        while(p2 != None):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
        
def buildList(num):
    head = None
    cur = None
    for i in range(num):
        node = ListNode(i)
        if head == None:
            head = node
            cur = node
            continue
        cur.next = node
        cur = node
    return head
def printList(head):
    cur = head
    while(cur != None):
        print(cur.val)
        cur = cur.next

if __name__ == '__main__':
    #head = ListNode(0)
    head = buildList(5)
    printList(head)
    
    s = Solution()
    head = s.reverseList(head)
    printList(head)
    pass
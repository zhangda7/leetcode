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
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
        if head == None:
            return
        if m == n:
            #early stop from here is easier
            return head
        cur = head
        #3 additional pointer: reverseBegin, pointer before reverseBegin, reverseEnd
        begin = cur
        end = None
        reverseBegin = cur
        count = 0
        for i in range(m - 1):
            begin = cur
            cur = cur.next
            reverseBegin = cur
        p1 = cur
        p2 = p1.next
        while(p2 != None):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            count += 1
            if count >= (n - m):
                break
        if begin != reverseBegin:
            begin.next = p1
            reverseBegin.next = p2
        else:
            head = p1
            begin.next = p2
        return head
        
def buildList(num):
    head = None
    cur = None
    for i in range(num):
        node = ListNode(i + 1)
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
    head = s.reverseBetween(head, 1, 1)
    printList(head)
    pass
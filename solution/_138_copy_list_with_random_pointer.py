# -*- coding:utf-8 -*-

'''
Created on 2015/8/13

@author: dazhang

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        dummy = RandomListNode(0)
        cur = head
        newCur = dummy
        table = {}
        while(cur != None):
            node = RandomListNode(cur.label)
            newCur.next = node
            node.random = cur.random
            #if cur.random != None:
            table[str(cur)] = node
            cur = cur.next
            newCur = newCur.next
        #print table
        newCur = dummy.next
        while(newCur != None):
            if newCur.random != None:
                #print newCur.random
                newCur.random = table[str(newCur.random)]
            newCur = newCur.next
        return dummy.next
        
        
def printList(head):
    if head == None:
        print("none")
    while(head != None):
        if head.random != None:
            print head.label, head.random.label
        else:
            print head.label
        head = head.next

if __name__ == '__main__':
    s1 = RandomListNode(1)
    s2 = RandomListNode(2)
    s3 = RandomListNode(3)
    s4 = RandomListNode(4)
    s5 = RandomListNode(5)
    s6 = RandomListNode(6)
    s1.next = s2
    s1.random = s3
    s2.next = s3
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s2.random = s6
    s3.random = s5
    s6.next = None
    #printList(s1)
    s = Solution()
    printList(s.RandomListNode(s1))
    pass
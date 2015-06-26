'''
Created on 2015/6/26

must use ListNode, singly-linked list

@author: dazhang
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        '''
        c1 : current node for l1
        c2 : current node for l2
        c3 : current node for new list
        head : head node for new list
        '''
        c1 = l1
        c2 = l2
        head = None
        c3 = None
        carry = 0
        while c1 != None and c2 != None:
            newC3 = ListNode((c1.val + c2.val + carry) % 10)
            if c3 == None:
                c3 = newC3
                head = c3
            else:
                c3.next = newC3
                c3 = newC3
            if (c1.val + c2.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            c1 = c1.next
            c2 = c2.next
        while c1 != None:
            newC3 = ListNode((c1.val + carry) % 10)
            c3.next = newC3
            c3 = newC3
            if (c1.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            c1 = c1.next
        while c2 != None:
            newC3 = ListNode((c2.val + carry) % 10)
            c3.next = newC3
            c3 = newC3
            if (c2.val + carry) >= 10:
                carry = 1
            else:
                carry = 0
            c2 = c2.next
        if carry != 0:
            newC3 = ListNode(carry)
            c3.next = newC3
        return head

def printList(l):
    while(l != None):
        print(l.val)
        l = l.next        
       
if __name__ == '__main__':
    pass
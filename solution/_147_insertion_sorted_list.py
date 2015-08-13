# -*- coding:utf-8 -*-

'''
Created on 2015/8/10

@author: dazhang

Sort a linked list using insertion sort.
'''
import time
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution2:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        if head == None:
            return None
        cur = head
        h = head
        next = head.next
        preOut = head
        changed = False
        while(cur != None):
            if not changed:
                preOut = cur
            cur = next
            if cur == None:
                break
            next = cur.next
            if preOut.val <= cur.val:
                continue
            
            
            h = head
            preIn = head
            while(h != None and h != cur):
                changed = False
                #printList(head)
                if h.val <= cur.val:
                    preIn = h
                else:
                    #insert here
                    if h == head:
                        preOut.next = cur.next
                        cur.next = h
                        head = cur
                        changed = True
                    else:
                        preOut.next = cur.next
                        preIn.next = cur
                        cur.next = h
                        changed = True
                    break
                h = h.next
        return head

class Solution:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        cur = head
        while(cur.next != None):
            if cur.next.val < cur.val:
                pre = dummy
                while(pre.next != None and pre.next.val <= cur.next.val):
                    pre = pre.next
                tmp = cur.next
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                cur = cur.next
        return dummy.next       
                

'''
This may be standand way to solve this.
'''
class Solution3:
# @param head, a ListNode
# @return a ListNode
    def insertionSortList(self, head):
        if not head:
            return head
        dummy = ListNode(0)                         #为链表加一个头节点
        dummy.next = head
        curr = head
        while curr.next:
            if curr.next.val < curr.val:            #如果链表是升序的，那么curr指针一直往后移动
                pre = dummy                         #直到一个节点的值小于前面节点的值
                while pre.next.val < curr.next.val: #然后寻找插入的位置
                    pre = pre.next
                tmp = curr.next                     #上面的示意图就是以下这段代码
                curr.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
            else:
                curr = curr.next
        return dummy.next

def printList(head):
    if head == None:
        print("none")
    while(head != None):
        print(head.val),
        head = head.next
    print ""

if __name__ == '__main__':
    s1 = ListNode(9)
    s2 = ListNode(9)
    s3 = ListNode(3)
    s4 = ListNode(1)
    s5 = ListNode(5)
    s6 = ListNode(6)
    s1.next = s2
    s2.next = None
    s3.next = s4
    s4.next = s5
    s5.next = s6
    s6.next = None
    s = Solution()
    printList(s.insertionSortList(s1))
    pass
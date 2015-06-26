'''
Created on 2015/6/26

@author: dazhang
'''
import unittest
from solution import _2_add_two_numbers

def createListNode(list):
    head = None
    cur = None
    for l in list:
        newNode = _2_add_two_numbers.ListNode(l)
        if cur == None:
            cur = newNode
            head = cur
        else:
            cur.next = newNode
            cur = newNode
    return head

def toList(listNode):
    ret = []
    while(listNode != None):
        ret.append(listNode.val)
        listNode = listNode.next
    return ret

class Test(unittest.TestCase):


    def testName(self):
        s = _2_add_two_numbers.Solution()
        self.assertEqual([0,1],toList(s.addTwoNumbers(createListNode([5]), createListNode([5]))))
        self.assertEqual([0,3,4],toList(s.addTwoNumbers(createListNode([5]), createListNode([5,2,4]))))
        self.assertEqual([5,2,4],toList(s.addTwoNumbers(createListNode([0]), createListNode([5,2,4]))))
        self.assertEqual([5,2,4],toList(s.addTwoNumbers(createListNode([5, 2 , 4]), createListNode([0]))))
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
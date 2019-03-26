# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        m = ListNode(0)
        head = m
        while l1 or l2:
            if l1 and not l2:
                m.next = l1
                return head.next
            elif not l1 and l2:
                m.next = l2
                return head.next
            elif l1.val < l2.val:
                m.next = ListNode(l1.val)
                l1 = l1.next
                m = m.next
            elif l1.val >= l2.val:
                m.next = ListNode(l2.val)
                l2 = l2.next
                m = m.next

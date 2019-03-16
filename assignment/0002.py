# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l = l1
        while l1 is not None or l2 is not None:
            if l2.next and not l1.next:
                l1.next = ListNode(0)
            if l1.next and not l2.next:
                l2.next = ListNode(0)
            l1.val = l1.val + l2.val
            if l1.val >= 10:
                l1.val -= 10
                if l1.next:
                    l1.next.val += 1
                else:
                    l1.next = ListNode(1)
                    l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
        return l


l3 = ListNode(3)
l3.next = ListNode(7)
Solution.addTwoNumbers(Solution(), ListNode(5), ListNode(5))



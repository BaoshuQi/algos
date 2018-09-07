# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        ept = ListNode(0)
        ept.next = head

        pre = ept
        while pre.next:
            if pre.next.val == val:
                pre.next = pre.next.next
                continue
            pre = pre.next

        return ept.next
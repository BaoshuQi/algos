# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        h = head
        c = 1
        while h.next:
            c += 1
            h = h.next
        s = c - n
        print(s)
        h = head
        if s == 0:
            return h.next
        for i in range (1, s):
            h = h.next
        t = h.next
        h.next = t.next
        return head
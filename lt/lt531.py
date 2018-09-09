# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        first = [root]
        while first:
            nxt = self.nextrow(first)
            if not nxt:
                return first[0].val
            first = nxt
        return None

    def nextrow(self, nodes):
        l = []
        for node in nodes:
            if node.left:
                l.append(node.left)
            if node.right:
                l.append(node.right)
        return l
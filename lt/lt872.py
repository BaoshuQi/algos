# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.bfs(root1) == self.bfs(root2)

    def bfs(self, root):
        l = list()
        if not root.left and not root.right:
            return [root.val]
        if root.left:
            l += self.bfs(root.left)
        if root.right:
            l += self.bfs(root.right)
        return l

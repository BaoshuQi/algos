# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        if root.left and root.right and self.equ(self.swap(root.right), root.left):
            return True
        elif not root.left and not root.right:
            return True
        return False

    def swap(self, root):
        # root.left or root.right:
        if not root:
            return root
        if not root.left and not root.right:
            return root
        root.left, root.right = root.right, root.left
        self.swap(root.left)
        self.swap(root.right)
        return root

    def equ(self, root1, root2):
        if root1 and root2:
            if root1.val == root2.val and self.equ(root1.left, root2.left) and self.equ(root1.right, root2.right):
                return True
        elif not root1 and not root2:
            return True
        return False


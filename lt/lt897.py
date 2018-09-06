# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        l = []

        def midrec(l, r):
            if r == None:
                return
            midrec(l, r.left)
            l.append(r.val)
            midrec(l, r.right)
            return l

        midrec(l, root)
        newTree = TreeNode(l[0])
        rt = newTree
        l.pop(0)
        while l:
            son = TreeNode(l.pop(0))
            newTree.right = son
            newTree = newTree.right
        return rt
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return list()
        l = list()
        lvl = list()
        lvl.append(root)

        while len(lvl) > 0:
            tmp = list()
            val = list()
            for son in lvl:
                if son.left:
                    tmp.append(son.left)
                if son.right:
                    tmp.append(son.right)
                val.append(son.val)
            lvl = tmp
            l.append(val)
        return l[::-1]


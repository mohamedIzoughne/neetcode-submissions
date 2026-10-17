# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root, maxisofar=float('-inf')):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        if root.val >= maxisofar:
            return 1 + self.goodNodes(root.left, root.val) + self.goodNodes(root.right, root.val)
        else:
            return self.goodNodes(root.left, maxisofar) + self.goodNodes(root.right, maxisofar)



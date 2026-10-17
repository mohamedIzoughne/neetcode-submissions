# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        sortedList = []
        def traverseTree(root):

            if root is None:
                return

            traverseTree(root.left)
            sortedList.append(root.val)
            traverseTree(root.right)

        traverseTree(root)
        # return sortedList[k - 1]
        return sortedList[k - 1]

        
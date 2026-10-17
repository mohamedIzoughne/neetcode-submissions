# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ordered_result = []

        def traverse(root):
            if (root is not None):
                traverse(root.left)
                ordered_result.append(root.val)
                traverse(root.right)

        traverse(root)

        for i in range(len(ordered_result) - 1):
            if ordered_result[i] >= ordered_result[i+1]:
                return False

        return True




        


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.left.val >= root.val:
            return False
        elif root.right and root.right.val <= root.val:
            return False

        if root.left and root.right:
            self.isValidBST(root.left)
            self.isValidBST(root.right)

        return True
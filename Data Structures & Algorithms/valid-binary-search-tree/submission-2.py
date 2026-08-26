# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inf = 1000000000 
        def isValid(node, minimum, maximum):
            if not node:
                return True
            elif node.left and (node.left.val >= node.val or node.left.val <= minimum):
                return False
            elif node.right and (node.right.val <= node.val or node.right.val >= maximum):
                return False

            return isValid(node.left, minimum, node.val) and isValid(node.right, node.val, maximum)

        return isValid(root, -inf, inf)
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
            if node.left and (node.left.val >= node.val or node.left.val <= minimum):
                return False
            elif node.right and (node.right.val <= node.val or node.right.val >= maximum):
                return False

            if node.left and node.right:
                isValid(node.left, -inf, node.val)
                isValid(node.right, node.val, inf)

            return True
        
        return isValid(root, -inf, inf) and isValid(root, -inf, inf)
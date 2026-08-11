# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # res = 0
        if root == None:
            return 0
        # elif root.left:
        #     res += 1
        # elif root.right:
        #     res += 1

        lmax = self.maxDepth(root.left)
        rmax = self.maxDepth(root.right)
        lmax += 1
        rmax += 1

        if lmax > rmax:
            return lmax
        else:
            return rmax
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = deque([])
        if not root:
            return res
        level.append(root)
        while level:
            step = []
            for i in range(len(level)):
                cur = level.popleft()
                step.append(cur.val)
                if cur.left and cur.right:
                    level.append(cur.left)
                    level.append(cur.right)
            res.append(step)
            


        return res
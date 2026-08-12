# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        pdeque = deque([p])
        qdeque = deque([q])
        while pdeque or qdeque:

            if (not pdeque and qdeque) or (pdeque and not qdeque):
                    return False
            for i in range(len(pdeque)):
                pnode = pdeque.popleft()
                qnode = qdeque.popleft()
                if (not pnode and qnode) or (pnode and not qnode):
                    return False
                elif not pnode and not qnode:
                    continue
                elif pnode.val != qnode.val:
                    return False
                if pnode.left or pnode.right:
                    pdeque.append(pnode.left)
                    pdeque.append(pnode.right)
                if qnode.left or qnode.right:
                    qdeque.append(qnode.left)
                    qdeque.append(qnode.right)
            

        return True
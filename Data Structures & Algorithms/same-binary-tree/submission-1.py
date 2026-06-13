# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            value = p.val == q.val
            if (p.left and not q.left) or (q.left and not p.left) or (p.right and not q.right) or (q.right and not p.right):
                return False
            if not p.left and not p.right:
                return value
            if not p.right:
                return helper(p.left, q.left) and value
            if not p.left:
                return helper(p.right, q.right) and value
            return helper(p.left, q.left) and helper(p.right, q.right) and value
        if not p and not q:
            return True
        if not p or not q:
            return False
        return helper(p, q)
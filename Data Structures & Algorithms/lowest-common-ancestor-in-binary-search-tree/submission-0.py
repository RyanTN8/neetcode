# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        small = min(p.val, q.val)
        big = max(p.val, q.val)

        while small > root.val or big < root.val:
            if small > root.val:
                root = root.right
            elif big < root.val:
                root = root.left
        return root


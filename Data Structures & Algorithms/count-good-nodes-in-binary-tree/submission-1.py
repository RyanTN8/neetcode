# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, maximum: int, goodNodes: int) -> int:
            good = goodNodes + (1 if node.val >= maximum else 0)
            if not node.left and not node.right:
                return good
            if not node.right:
                return dfs(node.left, max(maximum, node.val), good)
            if not node.left:
                return dfs(node.right, max(maximum, node.val), good)
            return dfs(node.left, max(maximum, node.val), 0) + dfs(node.right, max(maximum, node.val), 0) + good

        if not root:
            return 0
        return dfs(root, root.val, 0)
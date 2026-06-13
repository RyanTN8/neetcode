# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> (int, bool):
            if not root.left and not root.right:
                return (1, True)
            elif not root.right:
                depth, balanced = dfs(root.left)
                return (depth + 1, depth <= 1)
            elif not root.left:
                depth, balanced = dfs(root.right)
                return (depth + 1, depth <= 1)
            else:
                depthL, balancedL = dfs(root.left)
                depthR, balancedR = dfs(root.right)

                balanced = abs(depthL - depthR) <= 1 and balancedL and balancedR
                return (max(depthL, depthR) + 1, balanced )
        if not root:
            return True
        return dfs(root)[1]
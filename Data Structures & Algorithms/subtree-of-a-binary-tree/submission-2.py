# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            value = p.val == q.val
            #one tree has a branch but other doesn't
            if (p.left and not q.left) or (q.left and not p.left) or (p.right and not q.right) or (q.right and not p.right):
                return False
            if not p.left and not p.right:
                return value
            if not p.right:
                return sameTree(p.left, q.left) and value
            if not p.left:
                return sameTree(p.right, q.right) and value
            return sameTree(p.left, q.left) and sameTree(p.right, q.right) and value
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p.left and not p.right:
                return sameTree(p, q)
            if not p.right:
                return sameTree(p, q) or dfs(p.left, q)
            if not p.left:
                return sameTree(p, q) or dfs(p.right, q)
            else:
                return sameTree(p, q) or dfs(p.left, q) or dfs(p.right, q)
        return dfs(root, subRoot)

            
        
        

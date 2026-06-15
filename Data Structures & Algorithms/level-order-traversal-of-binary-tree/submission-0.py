# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def bfs(node: Optional[TreeNode], level: int, result: []) -> None:
            # create new level in result
            if level >= len(result):
                result.append([])
            # add node to current level
            result[level].append(node.val)
            # recurse on left node
            if node.left:
                bfs(node.left, level + 1, result)
            # recurse on right node
            if node.right:
                bfs(node.right, level + 1, result)
        if not root:
            return []
        bfs(root, 0, result)
        return result
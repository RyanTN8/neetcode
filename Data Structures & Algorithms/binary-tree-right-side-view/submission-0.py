# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def bfs(node: Optional[TreeNode], level: int, result: []) -> None:
            if level >= len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                bfs(node.left, level + 1, result)
            if node.right:
                bfs(node.right, level + 1, result)
        if not root:
            return []
        bfs(root, 0, result)
        for i in range(len(result)):
            result[i] = result[i][-1]
        return result
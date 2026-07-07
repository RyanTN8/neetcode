"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in visited:
                return visited[node]
            
            if not node:
                return None
            newNode = Node(node.val)
            visited[node] = newNode

            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    newNode.neighbors.append(dfs(neighbor))
            return newNode
        return dfs(node)
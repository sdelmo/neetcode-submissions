"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # memoize independent nodes so we don't recreate things

        memo = {}
        if not node: return None

        def adjlist_dfs(node):
            if node in memo:
                return memo[node]
            
            # Create a new node
            memo[node] = Node(node.val)

            # Fill and create its neighbours
            for nei in node.neighbors:
                memo[node].neighbors.append(adjlist_dfs(nei))
            return memo[node]
        
        adjlist_dfs(node)
        return memo[node]
        
        

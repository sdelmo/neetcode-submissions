"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        # memoize nodes so we don't recreate them
        memo = {}

        def dfs_adjlist(node):
            # If we are trying to create an already existing
            # Node, fetch it from the cache
            if node in memo:
                return memo[node]
            
            # Copy node into a new obj in memory
            memo[node] = Node(node.val)

            # Populate neighbors of the node
            for nei in node.neighbors:
                memo[node].neighbors.append(dfs_adjlist(nei))
            # return recursively copied node
            return memo[node]
        
        dfs_adjlist(node)
        return memo[node]
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
        
        cache = {} # set a cache to reuse copied nodes instead of recreating them

        def dfs(node):
            if node in cache:
                return cache[node]

            # copy node
            cache[node] = Node(node.val)

            # recreate neighbours of node and fill them into neighbors
            for nei in node.neighbors:
                cache[node].neighbors.append(dfs(nei))
            
            # return fully copied node to caller
            return cache[node]

        dfs(node)
        return cache[node]

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if node is None:
            return None

        queue = deque()
        visited = {}
        
        visited[node] = Node(node.val)

        queue.append(node)
        
        while queue:
            current = queue.popleft()

            for n in current.neighbors:
                if n not in visited:
                    visited[n] = Node(n.val)
                    queue.append(n)
                visited[current].neighbors.append(visited[n]) 
        return visited[node]
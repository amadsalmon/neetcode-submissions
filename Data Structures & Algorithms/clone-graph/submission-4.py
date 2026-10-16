"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import defaultdict, deque

class Solution:
    """
    Complexity: O(N+E)  (N number of nodes, E number of edges)
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        clones = { node: Node(node.val) }
        q = deque([node])

        while q:
            original = q.popleft()

            for original_neighbor in original.neighbors:
                if original_neighbor not in clones:
                    clones[original_neighbor] = Node(original_neighbor.val)
                    q.append(original_neighbor)
                clones[original].neighbors.append(clones[original_neighbor])

        return clones[node]


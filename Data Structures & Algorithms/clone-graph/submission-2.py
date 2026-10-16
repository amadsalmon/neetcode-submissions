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
    Complexity O(N+E)  (N number of nodes, E number of edges)
    """
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        def clone(node: Node) -> Node:
            """Deep clones a node without its neighbors"""
            return Node(node.val)

        if not node: return None

        clones = defaultdict()
        q = deque()
        q.append(node)

        while q:
            original = q.popleft()
            if original not in clones:
                cloned = clone(original)
                clones[original] = cloned
            else:
                continue

            for original_neighbor in original.neighbors:
                q.append(original_neighbor)

        for original, clone in clones.items():
            for n in original.neighbors:
                clone.neighbors.append(clones[n])

        return clones[node]
  
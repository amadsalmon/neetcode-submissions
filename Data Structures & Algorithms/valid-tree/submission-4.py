from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Build adjacency list
        adj = defaultdict(list)
        for edge_a, edge_b in edges:
            adj[edge_a].append(edge_b)
            adj[edge_b].append(edge_a)
        
        if len(edges) != n - 1:
            return False

        seen = set()

        def dfs(node: int, parent: int):
            seen.add(node)
            for neighbor in adj[node]:
                if neighbor != parent:
                    if neighbor in seen:
                        return False
                    
                    if not dfs(neighbor, node):
                        return False
            return True
        
        return dfs(0, 0) and len(seen) == n

        
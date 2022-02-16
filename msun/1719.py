from collections import defaultdict
class Solution:
    def checkWays(self, pairs: list) -> int:
        adj = defaultdict(list)
        for x, y in pairs:
            adj[x].append(y)
            adj[y].append(x)
        
        root = next((node for node, neighbors in adj.items() if len(neighbors) == len(adj) - 1), -1)
        if root == -1:
            return 0
        
        ans = 1
        for node, neighbors in adj.items():
            if node == root:
                continue

            current_deg = len(neighbors)
            parent = -1

            parent_deg = 1e6
            for neighbor in neighbors:
                if current_deg <= len(adj[neighbor]) < parent_deg:
                    parent = neighbor
                    parent_deg = len(adj[neighbor])
            
            if parent == -1 or any(neighbor != parent and neighbor not in adj[parent] for neighbor in neighbors):
                return 0
            
            if parent_deg == current_deg:
                ans = 2
        return ans
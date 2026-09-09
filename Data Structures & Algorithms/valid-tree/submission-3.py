class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)

        if not edges:
            return True
        
        if len(edges) > n - 1:
            return False

        
        for src, dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()

        def dfs(src, prev):
            if src in visited:
                return False
            visited.add(src)
            for j in adj[src]:
                if j == prev:
                    continue
                if not dfs(j, src):
                    return False
            return True
        dfs(0,-1)
        return False if len(visited) < n else True





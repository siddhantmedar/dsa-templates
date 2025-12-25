# 323. Number of Connected Components in an Undirected Graph
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(start, visited):
            visited[start] = 1
            for neighbour in hmap[start]:
                if visited[neighbour] == 0:
                    dfs(neighbour, visited)
            
        
        hmap = defaultdict(list)
        
        count = 0
        visited = [0]*n
        
        for u,v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        
        for i in range(n):
            if visited[i] == 0:
                dfs(i, visited)
                count+=1
                
        return count
            
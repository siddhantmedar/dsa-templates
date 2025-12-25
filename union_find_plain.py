class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            setx = find(x)
            sety = find(y)
            
            if setx != sety:
                parent[sety] = setx
            
        parent = {i:i for i in range(n)}
        
        for u,v in edges:
            union(u,v)
        
        count = 0
        
        for k,v in parent.items():
            if k==v:
                count+=1
        
        return count
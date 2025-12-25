# 1135. Connecting Cities With Minimum Cost

import heapq

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]
        
        def union(city1, city2):
            root1, root2 = find(city1), find(city2)
            
            if root1 == root2:
                return False
            parent[root2] = root1
            return True
        parent = {city:city for city in range(1, n+1)}
        
        connections.sort(key = lambda x : x[2])
        
        totalcost = 0
        
        for city1, city2, cost in connections:
            if union(city1, city2):
                totalcost+=cost
        
        ref = find(n)
        return totalcost if all(ref == find(city) for city in range(1, n+1)) else -1
    
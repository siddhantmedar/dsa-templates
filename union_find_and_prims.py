# 1135. Connecting Cities With Minimum Cost

import heapq 

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        m = collections.defaultdict(list)
        for city1, city2, cost in connections:
            m[city1].append((cost, city2))
            m[city2].append((cost, city1))
        
        queue = [(0, N)]
        visited = set()
        
        total = 0
        
        while queue and len(visited) < N:
            cost, city = heapq.heappop(queue)
            if city not in visited:
                visited.add(city)
                total+=cost
                for ncost, ncity in m[city]:
                    heapq.heappush(queue, (ncost, ncity))
        return total if len(visited) == N else -1
        
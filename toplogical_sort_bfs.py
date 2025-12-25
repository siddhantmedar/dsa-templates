#Topological Sort - DFS Approach
from collections import deque

graph = {
    0:[],
    1:[],
    2:[3],
    3:[1],
    4:[0,1],
    5:[0,2]
}

indegree = [0]*6
result = []
queue = deque()
stack = []

#get the indegree count of all the nodes in the graph
for node, adj in graph.items():
    for adj_nodes in adj:
        indegree[adj_nodes]+=1

for i in range(len(indegree)):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    result.append(node)
    for adj_nodes in graph[node]:
        indegree[adj_nodes]-=1
        if indegree[adj_nodes] == 0:
            queue.append(adj_nodes)

print(result)
print(len(queue) == 0)
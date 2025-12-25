from collections import deque

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [2]
}

indegree = [0] * len(graph)
queue = deque()

for _, adj in graph.items():
    for adjs in adj:
        indegree[adjs] += 1

for i in range(len(graph)):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()

    for adj in graph[node]:
        indegree[adj] -= 1
        if indegree[adj] == 0:
            queue.append(adj)

if len(queue):
    print("No cycle")
else:
    print("Cycle exists!")

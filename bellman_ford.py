graph = [(0, 1, -1),
         (0, 2, 4),
         (1, 2, 3),
         (1, 3, 2),
         (1, 4, 2),
         (3, 2, 5),
         (3, 1, 1),
         (4, 3, -3)
         ]

V = 5
isNegCycle = False
dist = [float("inf")] * V
dist[0] = 0

for _ in range(V - 1):
    for u, v, weight in graph:
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight

for u, v, weight in graph:
    if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        isNegCycle = True
        print("Negative edge is present!")

if not isNegCycle:
    print("No negative edge cycle is present")

# ====================================================================
# Negative edge cycle graph

graph = [(0, 1, 1),
         (1, 2, -1),
         (2, 3, -1),
         (3, 0, -1),
         (1, 4, 2),
         (3, 2, 5),
         (3, 1, 1),
         (4, 3, -3)
         ]

V = 5
isNegCycle = False
dist = [float("inf")] * V
dist[0] = 0

for _ in range(V - 1):
    for u, v, weight in graph:
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight

for u, v, weight in graph:
    if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        isNegCycle = True
        print("Negative edge is present!")

if not isNegCycle:
    print("No negative edge cycle is present")

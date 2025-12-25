from collections import deque, defaultdict

graph = {
    1:[2],
    2:[3,4],
    3:[1],
    4:[5],
    5:[]
}

# Steps:
# 1->Topo
# 2->Tranpose
# 3_>DFS of rev graph

visited = [False]*(len(graph)+1)
stack = deque()

def dfs(node):
    visited[node] = True

    for nd in graph[node]:
        if visited[nd] == False:
            dfs(nd)
    stack.append(node)

for i in range(1, len(graph)):
    if visited[i] == False:
        dfs(i)

#Tranpose the graph

rev_graph = defaultdict(list)

for node, adj in graph.items():
    for adj_nodes in adj:
        visited[adj_nodes] = False
        rev_graph[adj_nodes].append(node)

stack.reverse()

result = []
tmp = []

def revdfs(node):
    visited[node] = True
    tmp.append(node)

    for adj in rev_graph[node]:
        if not visited[adj]:
            revdfs(adj)


while stack:
    node = stack.popleft()
    if not visited[node]:
        revdfs(node)
        result.append(tmp.copy())
        tmp.clear()

print(result)
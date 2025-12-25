#Topological Sort - DFS Approach
graph = {
    0:[],
    1:[],
    2:[3],
    3:[1],
    4:[0,1],
    5:[0,2]
}

visited = [False]*6
stack = []

def dfs(node):
    visited[node] = True

    for nd in graph[node]:
        if visited[nd] == False:
            dfs(nd)
    stack.append(node)

for i in range(6):
    if visited[i] == False:
        dfs(i)

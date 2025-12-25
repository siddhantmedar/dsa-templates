from collections import deque

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

isCycle = False
visited = [False] * len(graph)


def dfs(node, parent):
    visited[node] = True

    for adj in graph[node]:
        if not visited[adj]:
            dfs(adj, node)
        elif adj != parent:
            return 1
    return 0


if __name__ == "__main__":

    for i in range(len(graph)):
        if not visited[i]:
            if dfs(i, -1) == 1:
                isCycle = True

    if isCycle:
        print("Cycle exists!")
    else:
        print("No cycle found!")
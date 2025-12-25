from collections import deque

graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [2]
}

isCycle = False
visited = [0] * len(graph)


def dfs(node, parent):
    visited[node] = 1

    for adj in graph[node]:
        if not visited[adj]:
            return dfs(adj, node)
        elif visited[adj] == 1:
            return 1
    visited[node] = 2
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

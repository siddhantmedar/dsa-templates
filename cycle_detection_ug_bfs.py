from collections import deque

graph = {
    0: [1],
    1: [0, 2],
    2: [1]
}

isCycle = False

visited = [False] * len(graph)


def bfs(node, parent):
    queue = deque()
    queue.append([node, parent])
    visited[node] = True

    while queue:
        node, parent = queue.popleft()

        for adj in graph[node]:
            if not visited[adj]:
                queue.append([adj, node])
                visited[adj] = True
            elif adj != parent:
                return 1
    return 0


if __name__ == "__main__":

    for i in range(len(graph)):
        if not visited[i]:
            if bfs(i, -1) == 1:
                isCycle = True

    if isCycle:
        print("Cycle exists!")
    else:
        print("No cycle found!")
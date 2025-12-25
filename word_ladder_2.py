import copy
from collections import defaultdict, deque


def wordLadder2(startword, endword, lst):
    result = []
    path = []

    def DFS(startword, endword, adj):
        path.append(startword)
        if startword == endword:
            result.append(copy.deepcopy(path))
            path.pop()
            return

        for neighbour in adj[startword]:
            DFS(neighbour, endword, adj)
        path.pop()

    adj = defaultdict(list)
    st = set(lst)
    visited = {}
    q = deque()
    q.append(startword)
    visited[startword] = 0

    while q:
        node = q.popleft()
        tmp = copy.deepcopy(node)
        for i in range(len(tmp)):
            for c in range(97, 123):
                if tmp[i] == chr(c):
                    continue
                tmp = list(tmp)
                tmp[i] = chr(c)
                tmp = "".join(tmp)
                if tmp in st:
                    if tmp not in visited:
                        visited[tmp] = 1 + visited[node]
                        q.append(tmp)
                        adj[node].append(tmp)
                    elif visited[tmp] == visited[node] + 1:
                        adj[node].append(tmp)
            tmp = list(tmp)
            tmp[i] = node[i]
    # path = []
    DFS(startword, endword, adj)
    return result


lst = ["hot", "dot", "dog", "lot", "log", "cog"]
print(wordLadder2("hit", "cog", lst))

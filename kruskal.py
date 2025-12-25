import heapq


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    setX = find(a)
    setY = find(b)

    if setX != setY:
        parent[setY] = setX
        return True
    else:
        return False


V = 6

parent = {i: i for i in range(1, V + 1)}

graph = [
    (1, 1, 4),
    (2, 1, 2),
    (3, 2, 3),
    (3, 2, 4),
    (4, 1, 5),
    (5, 3, 4),
    (7, 2, 6),
    (8, 3, 6),
    (9, 4, 5)
]

lst = sorted(graph, key=lambda x: x[0])
res = list()
st = set()

while len(st) != V:
    item = heapq.heappop(lst)
    if union(item[1], item[2]):
        res.append(item)
        st.add(item[1])
        st.add(item[2])

print("MST:", res)

# ==============================================================
# Another graph
print("\n")

graph = [
    (2, 1, 2),
    (4, 1, 3),
    (1, 2, 3)
]

V = 3
parent = {i: i for i in range(1, V + 1)}

lst = sorted(graph, key=lambda x: x[0])
res = list()
st = set()

while len(st) != V:
    item = heapq.heappop(lst)
    if union(item[1], item[2]):
        res.append(item)
        st.add(item[1])
        st.add(item[2])

print("MST:", res)
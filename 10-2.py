def findParent(parent, x):
    if parent[x] != x:
        parent[x] = findParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = findParent(parent, a)
    b = findParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

graph = []
result = []

for i in range(1, n + 1):
    parent[i] = i

# a = 출발 / b = 도착 / c = 비용
for i in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

graph = sorted(graph, key = lambda x : x[2])

for node in graph:
    a, b, c = node
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result.append(c)

result.sort(reverse = True)
print(sum(result[1:]))
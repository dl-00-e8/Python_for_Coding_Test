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


n = int(input())
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

xList = []
yList = []
zList = []
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    xList.append((x, i))
    yList.append((y, i))
    zList.append((z, i))

xList.sort()
yList.sort()
zList.sort()

edges = []
result = 0
for i in range(n - 1):
    edges.append((xList[i + 1][0] - xList[i][0], xList[i][1], xList[i + 1][1]))
    edges.append((yList[i + 1][0] - yList[i][0], yList[i][1], yList[i + 1][1]))
    edges.append((zList[i + 1][0] - zList[i][0], zList[i][1], zList[i + 1][1]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if findParent(parent, a) != findParent(parent, b):
        unionParent(parent, a, b)
        result += cost

print(result)
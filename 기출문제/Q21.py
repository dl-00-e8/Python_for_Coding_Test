import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, i, j, visited):
    q = deque([(i, j)])
    visited[i][j] = True
    result = [(i, j)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < n):
                if (left <= abs(graph[nx][ny] - graph[x][y]) <= right):
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        result.append((nx, ny))
                        q.append((nx, ny))

    sum = 0
    for x, y in result:
        sum += graph[x][y]
    total = sum // len(result)
    for x, y in result:
        graph[x][y] = total


def checkOpen(graph, left, right):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < n) and (0 <= ny < n):
                    if (left <= abs(graph[nx][ny] - graph[x][y]) <= right):
                        return True

    return False


n, left, right = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

visited = [[False] * (n) for _ in range(n)]

cnt = 0
while True:
    if not checkOpen(graph, left, right):
        break

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(graph, i, j, visited)

    visited = [[False] * (n) for _ in range(n)]
    cnt += 1

print(cnt)
from collections import deque

n, k = map(int, input().split())

data = []
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] > 0:
            # 바이러스 타입, x좌표, y좌표 순
            data.append((graph[i][j], i, j, 0))
    
s, x, y = map(int, input().split())

# 상, 하, 좌, 우 방향 리스트
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    virusNum, a, b, time = q.popleft()
    
    # 시간 일치할 경우, 탈출
    if time == s:
        break
        
    # 작은 번호부터 순서대로 바이러스 전염 진행
    for i in range(4):
        na = a + dx[i]
        nb = b + dy[i]
        if 0 <= na and na < n and 0 <= nb and nb < n and graph[na][nb] == 0:
            graph[na][nb] = virusNum
            q.append((virusNum, na, nb, time + 1))

print(graph[x -1][y - 1])
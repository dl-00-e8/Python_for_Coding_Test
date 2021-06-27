from collections import deque
import copy

n = int(input())

inClass = [0] * (n + 1)
classTime = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    classTime[i] = data[0]
    for j in range(1, len(data) - 1):
        inClass[i] += 1
        graph[j].append(i)


def topologySort(n):
    # clasTime과 result사이의 얕은 복사로 서로 영향을 미치지 않게 하기 위해서 깊은 복사를 해야함
    result = copy.deepcopy(classTime)
    q = deque()

    for i in range(1, n + 1):
        if inClass[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for i in graph[now]:
            result[i] = max(result[i], result[now] + classTime[i])
            inClass[i] -= 1
            if inClass[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])
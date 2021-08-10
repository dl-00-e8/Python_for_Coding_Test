from itertools import combinations


def check(x, y, direction):
    if direction == 0:
        while y >= 0:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            y -= 1
    elif direction == 1:
        while y < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            y += 1
    elif direction == 2:
        while x >= 0:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            x -= 1
    elif direction == 3:
        while x < n:
            if graph[x][y] == 'S':
                return True
            elif graph[x][y] == 'O':
                return False
            x += 1

    return False


def checkAll():
    for nx, ny in teachers:
        for i in range(4):
            if check(nx, ny, i):
                return True

    return False


n = int(input())

graph = []
teachers = []
spaces = []
for i in range(n):
    graph.append(list(map(str, input().split())))
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'X':
            spaces.append((i, j))

find = False
for data in combinations(spaces, 3):
    for x, y in data:
        graph[x][y] = 'O'

    if not checkAll():
        find = True
        break

    for x, y in data:
        graph[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
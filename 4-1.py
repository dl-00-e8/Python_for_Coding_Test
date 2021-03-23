n = int(input())
plan = list(map(str, input().split()))

x, y = 1, 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in plan:
    if i == 'L':
        x = x + dx[0]
        y = y + dy[0]
        if y < 1:
            y = y - dy[0]
    elif i == 'R':
        x = x + dx[1]
        y = y + dy[1]
        if y > n:
            y = y - dy[1]
    elif i == 'U':
        x = x + dx[2]
        y = y + dy[2]
        if x < 1:
            x = x - dx[2]
    elif i == 'D':
        x = x + dx[3]
        y = y + dy[3]
        if x > n:
            x = x - dx[3]

print(x, y)
data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

moves = [(-1, 2), (1, 2), (-2, 1), (-2, -1), (-1, -2),(1, -2), (2, -1), (2, 1)]

cnt = 0
for move in moves:
    x, y = row, column
    x = x + move[0]
    y = y + move[1]
    if 1 <= x and x <= 8 and 1 <= y and y <= 8:
        cnt += 1

print(cnt)
n, m = map(int, input().split()) # n * m 입력

data = [[0] * m for _ in range(n)]
x, y, d = map(int, input().split())
data[x][y] = 1 # 시작 좌표 방문하였음을 의미

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# 좌표 상태 입력

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 1번 매뉴얼
def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

# 2, 3번 매뉴얼
def check(num):
    global d
    if num == 2:
        nx = x + dx[d]
        ny = y + dy[d]
        if data[nx][ny] == 1 or arr[nx][ny] == 1:
            return False
        else:
            return True
    elif num == 3:
        nx = x - dx[d]
        ny = y - dy[d]
        if arr[nx][ny] == 1:
            return False
        else:
            return True

cnt = 1
turn_cnt = 0
while True:
    turn_left()
    if check(2) == True:
        x = x + dx[d]
        y = y + dy[d]
        data[x][y] = 1
        cnt += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
    if turn_cnt == 4:
        if check(3) == True:
            x = x - dx[d]
            y = y - dy[d]
        else:
            break
        turn_cnt = 0
        
print(cnt)

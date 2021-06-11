n, m = map(int, input().split())
ball = list(map(int, input().split()))


def combination(n):
    up = 1
    for i in range(n, n-2, -1):
        up *= i
    down = 2
    
    return up // down


def checkSame(list, m):
    data = 0
    for i in range(1, m + 1):
        if list.count(i) >= 2:
            data += combination(list.count(i))

    return data

print(combination(n) - checkSame(ball, m))

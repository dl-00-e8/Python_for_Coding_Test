n, c = map(int, input().split())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()

start = 1
end = data[-1] - data[0]
result = []

while start <= end:
    first = data[0]
    mid = (start + end) // 2
    cnt = 1
    
    for i in range(1, n):
        if first + mid <= data[i]:
            first = data[i]
            cnt += 1

    if cnt >= c:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1

print(max(result))

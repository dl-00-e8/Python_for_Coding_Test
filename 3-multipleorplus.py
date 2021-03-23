data = list(map(int, input()))
result = data[0]

for i in range(1, len(data)):
    if result <= 1 or data[i] <= 1:
        result += data[i]
    else:
        result *= data[i]
        print(result)

print(result)

'''
1일 경우, 곱하면 원상태를 유지하지만
더하면 값이 증가할 수 있으므로, 더하기도 들어가야함'''
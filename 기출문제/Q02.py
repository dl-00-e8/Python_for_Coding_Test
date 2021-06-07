data = list(map(int, input()))

result = 0
for i in data:
    if result == 0:
        result += i
    elif i == 0 or i == 1:
        result += i
    else:
        result *= i

print(result)
data = list(map(int, input()))

zero_cnt = 0
one_cnt = 0
temp = data[0]
for i in range(1, len(data)):
    if temp == data[i]:
        temp = data[i]
        continue
    elif temp != data[i] and temp == 0:
        temp = data[i]
        zero_cnt += 1
    elif temp != data[i] and temp == 1:
        temp = data[i]
        one_cnt += 1

print(min(zero_cnt, one_cnt))
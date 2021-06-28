string = input()

result = []
num = 0
for i in string:
    if 65 <= ord(i) and ord(i) <= 90:
        result.append(i)
    elif 48 <= ord(i) and ord(i) <= 57:
        num += int(i)

result.sort()
result = ''.join(result)
print(result + str(num))


'''
# 숫자가 하나도 입력되지 않았을 경우 구분하여야 할 때
string = input()

result = []
num = 0
cnt = 0
for i in string:
    if 65 <= ord(i) and ord(i) <= 90:
        result.append(i)
    elif 48 <= ord(i) and ord(i) <= 57:
        num += int(i)
        cnt += 1

result.sort()
result = ''.join(result)
if cnt != 0:
    print(result + str(num))
else:
    print(result)
'''

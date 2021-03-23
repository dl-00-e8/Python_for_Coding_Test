n, m = map(int, input().split())
cnt = 0

while n != 1:
    if n % m != 0:
        n = n - 1
        cnt += 1
    else:
        n =  n // m
        cnt += 1

print(cnt)

'''
큰 수일때에도 빠르게 동작하기 위해선 일일이 1씩 빼는 것이 아닌 n이 k의 배수가 되도록 한번에 뺄 수 있게 코드를 변경할 수 있어야함
즉, n의 범위에 대한 주의가 필요함
'''
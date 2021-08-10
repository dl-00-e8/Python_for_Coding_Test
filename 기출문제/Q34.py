n = int(input())
soldiers = list(map(int, input().split()))

soldiers.reverse()

# 본인이 최장 증가 부분 수열의 시작이라는 기준으로 최장 길이 수열 값 세팅
length = [1] * n

# 최장 증가 부분 수열 찾기
for i in range(1, len(soldiers)):
    for j in range(0, i):
        if(soldiers[j] < soldiers[i]):
            length[i] = max(length[i], length[j] + 1)

print(n - max(length))
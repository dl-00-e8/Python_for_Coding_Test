from itertools import combinations

n, m = map(int, input().split())

# 집, 치킨집의 좌표 저장
house = []
chicken = []
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            house.append([i + 1, j + 1])
        elif data[j] == 2:
            chicken.append([i + 1, j + 1])


def distance(a, b):
    dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return dist


# 도시의 치킨 거리를 계산하는 함수
def chickenDistance(house, chicken, types):
    total = 99999

    for i in range(len(chicken)):
        result = [99999] * len(house)
        # 순열의 결과데이터가 1일 때
        if types == 1:
            for j in range(len(house)):
                result[j] = min(result[j], distance(chicken[i], house[j]))
            total = min(total, sum(result))
        # 순열의 결과데이터가 2개 이상일 때
        else:
            for j in chicken[i]:
                for k in range(len(house)):
                    result[k] = min(result[k], distance(j, house[k]))
            total = min(total, sum(result))

    return total


answer = 987654321
answer = min(answer, chickenDistance(house, chicken, 1))
if m >= 2:
    for i in range(2, m + 1):
        chooseChicken = list(combinations(chicken, i))
        answer = min(answer, chickenDistance(house, chooseChicken, 2))

print(answer)
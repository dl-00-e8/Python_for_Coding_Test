import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    queue = []
    for i in range(len(food_times)):
        heapq.heappush(queue, (food_times[i], i + 1))

    sumValue = 0
    before = 0
    length = len(food_times)

    while sumValue + ((queue[0][0] - before) * length) <= k:
        now = heapq.heappop(queue)[0]
        sumValue += (now - before) * length
        length -= 1
        before = now

    result = sorted(queue, key = lambda x : x[1])
    answer = result[(k - sumValue) % length][1]
    return answer

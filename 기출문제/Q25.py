from bisect import bisect_left, bisect_right

def solution(N, stages):
    answer = []
    failRate = []
    stages.sort()

    for i in range(N):
        users = len(stages) - bisect_left(stages, i + 1)
        if users == 0:
            failRate.append([i + 1, 0])
        else:
            failers = bisect_right(stages, i + 1) - bisect_left(stages, i + 1)
            failRate.append([i + 1, failers / users])
    
    failRate = sorted(failRate, key = lambda x : x[1], reverse = True)
    answer = [i[0] for i in failRate]
    
    return answer
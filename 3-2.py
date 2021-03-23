n, m, k = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)

if arr[0] == arr[1]:
    result = arr[0] * m
else:
    result = (arr[0] * k * (m // k)) + (arr[1] * (m % k))

print(result)
'''
입력방식 헷갈리지 말 것
처음에는 for문으로 입력을 받으려고 하였다가
공백 구분이라는 조건을 만족시키지 못하였었음

추가로 내림차순 정렬에서 쓰는 sorted의 사용 방식은
arr.sorted 가 아닌 sorted(arr, option)의 방식이다.

구현까지 걸린 시간 : 20분 
'''
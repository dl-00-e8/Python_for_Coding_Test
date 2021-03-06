import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    total = one + two
    result += total
    heapq.heappush(heap, total)

print(result)
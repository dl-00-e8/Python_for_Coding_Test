n = int(input())
house = list(map(int, input().split()))

house.sort()
mid = len(house)//2
print(house[mid - 1])
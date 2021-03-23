n, m = map(int, input().split())

card = []
minnum = []

for i in range(n):
    card = list(map(int, input().split()))
    minnum.append(min(card))
    card = []

print(max(minnum))
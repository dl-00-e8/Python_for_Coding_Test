n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i] < b[i]:
        temp = b[i]
        b[i] = a[i]
        a[i] = temp
    else:
        break

print(sum(a))
n = int(input())

sequence = []
for _ in range(n):
    sequence.append(int(input()))

sequence = sorted(sequence, reverse = True)
print(*sequence)
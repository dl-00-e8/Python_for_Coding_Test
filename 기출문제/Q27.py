from bisect import bisect_left, bisect_right


def counting(numbers, number):
    left = bisect_left(numbers, number)
    right = bisect_right(numbers, number)
    
    if right == left:
        return -1
    return right - left

n, x = map(int, input().split())

sequence = list(map(int, input().split()))

print(counting(sequence, x))
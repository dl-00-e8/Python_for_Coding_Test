mny = int(input("거스름돈을 입력해주세요. : "))
cnt = 0

for i in [500, 100, 50, 10]:
    cnt = cnt + (mny // i)
    mny = mny % i

print(cnt)
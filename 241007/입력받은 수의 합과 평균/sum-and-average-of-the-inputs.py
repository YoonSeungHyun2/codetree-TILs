num = int(input())

sum = 0
cnt = 0

for i in range(num):
    i = int(input())

    sum += i
    cnt += 1

ave = sum / cnt

print(sum, f"{ave:.1f}")
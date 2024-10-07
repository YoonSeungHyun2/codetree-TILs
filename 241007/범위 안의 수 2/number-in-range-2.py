sum = 0
cnt = 0
for i in range(10):
    n = int(input())
    if 0 <= n <= 200:
        
        sum += n
        cnt += 1

ave = sum / cnt
print(sum, f"{ave:.1f}")
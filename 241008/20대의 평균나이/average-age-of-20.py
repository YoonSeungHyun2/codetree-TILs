age = 0
cnt = 0

while True:
    n = int(input())
    
    if 20 <= n < 30:
        age += n
        cnt += 1
    else:
        break

print(f"{age/cnt:.2f}")
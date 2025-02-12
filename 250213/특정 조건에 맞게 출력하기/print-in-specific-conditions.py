numbers = list(map(int, input().split()))

result = []
for num in numbers:
    if num == 0:  # 0일 경우
        break
    if num % 2 == 0: # 짝수일 경우
        result.append(num // 2)
    else:  # 홀수일 경우
        result.append(num + 3)

print(*result)

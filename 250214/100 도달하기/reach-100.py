numbers = list(map(int, input().split()))

result = []
for num in numbers:
    if num == 0:
        break  # 0이 입력되면 반복 종료
    if num % 2 == 0:
        result.append(num // 2)  # 짝수면 2로 나눈 몫
    else:
        result.append(num + 3)  # 홀수면 3을 더함

print(*result)
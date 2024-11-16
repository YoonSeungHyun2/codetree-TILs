# 입력받기
numbers = list(map(int, input().split()))

# 0이 나올 때까지의 값을 추출
valid_numbers = []
for num in numbers:
    if num == 0:
        break
    valid_numbers.append(num)

# 합과 평균 계산
total = sum(valid_numbers)
average = total / len(valid_numbers) if valid_numbers else 0  # 비어 있는 경우 평균은 0으로 처리

# 출력
print(f"{total} {round(average, 1)}")

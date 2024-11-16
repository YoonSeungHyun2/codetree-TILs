# 입력받기
numbers = list(map(int, input().split()))

# 0이 나올 때까지의 값을 추출
multiples_of_two  = []
for num in numbers:
    if num == 0:
        break
    if num % 2 == 0:
        multiples_of_two.append(num)

# 합과 평균 계산
count = len(multiples_of_two)
total = sum(multiples_of_two)
# 출력
print(f"{count} {total}")

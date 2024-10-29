# 입력 처리: start와 end를 공백으로 구분하여 입력받음
start, end = map(int, input().split())

# 완전수 판별 함수 정의
def is_perfect_number(n):
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    return divisor_sum == n

# 완전수 개수 세기
perfect_count = 0
for num in range(start, end + 1):
    if is_perfect_number(num):
        perfect_count += 1

# 결과 출력
print(perfect_count)
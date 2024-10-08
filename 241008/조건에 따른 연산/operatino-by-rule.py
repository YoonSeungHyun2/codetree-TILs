# n = int(input())
# cnt = 0
# while n < 1000:
#     if n % 2 == 0:
#         n = n * 3 + 1
#     else:
#         n = n * 2 + 1
#     cnt += 1

# print(cnt)

# n을 입력받기
n = int(input())
cnt = 0

# n이 1000 미만인 동안 반복
while n < 1000:
    if n % 2 == 0:  # 짝수인 경우
        n = n * 3 + 1
    else:  # 홀수인 경우
        n = n * 2 + 2
    cnt += 1  # 연산 횟수 증가

# 결과 출력
print(cnt)
n = int(input())
cnt = 0

while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    cnt += 1

print(cnt)
        
# n = int(input())
# cnt = 0

# while n != 1:  # N이 1이 아닐 때까지 반복
#     if n % 2 == 0:
#         n //= 2  # N이 짝수인 경우
#     else:
#         n = n * 3 + 1  # N이 홀수인 경우
#     cnt += 1  # 반복 횟수 증가

# print(cnt)  # 최종 반복 횟수 출력
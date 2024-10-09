def solution(n):
    satisfied = True

    for i in range(1, n+1):
        if n % i == 0:
            satisfied = False
    
    if satisfied == True:
        print("P")
    else:
        print("C")

n = int(input())
solution(n)

# def solution(n):
#     # n이 소수인지 판별
#     if n < 2:  # 2보다 작은 수는 소수가 아님
#         print("C")
#         return

#     # 2와 n은 소수이므로, 3부터 sqrt(n)까지 나누어보며 검사
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:  # 나누어 떨어지는 경우
#             print("C")
#             return
    
#     # 위의 조건을 모두 통과한 경우
#     print("P")

# # 입력 받기
# n = int(input())
# solution(n)
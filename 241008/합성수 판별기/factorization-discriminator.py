# def solution(n):
#     if 2 <= n <= (n-1):
#         n = add

#         for i in range(n):
#             if n == add:
#                 print("c")
#             else:
#                 print("N")
# n = int(input))
# solution(n)

def solution(n):
    # n이 합성수인지 확인
    for i in range(2, n):  # 2부터 n-1까지 검사
        if n % i == 0:     # n이 i로 나누어 떨어지면 합성수
            print("C")
            return
    # 나누어 떨어지는 수가 없으면 소수
    print("N")

# n을 입력받기
n = int(input())
solution(n)